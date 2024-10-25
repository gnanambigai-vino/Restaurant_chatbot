from django.shortcuts import render
from .models import Order
from django.shortcuts import render
from django.http import HttpResponse
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')  # For tokenization
nltk.download('wordnet')  # For lemmatization

def index(request):
    return render(request, 'chatbot/index.html')

def preprocess_message(message):
    lemmatizer = WordNetLemmatizer()
    tokens = nltk.word_tokenize(message.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens

def chatbot_response(request):
    if request.method == "POST":
        user_message = request.POST.get('user_message', '').lower()
        processed_message = preprocess_message(user_message)
        response = ""
        user_name = 'guest_user'  # Placeholder for user identification
        active_order = Order.objects.filter(user_name=user_name).order_by('-created_at').first()

        if any(word in processed_message for word in ["hi", "hello"]):
            response = "Hello! How can I assist you today?"
        elif "menu" in processed_message:
            response = "Here is the menu: Pizza, Pasta, Salad. What would you like to order?"
        elif "order" in processed_message:
            item_ordered = next((item for item in ["pizza", "pasta", "salad"] if item in processed_message), None)
            if item_ordered:
                new_order = Order(user_name=user_name, item=item_ordered, status='preparing')
                new_order.save()
                response = f"Order placed! Your {item_ordered} is being prepared."
            else:
                response = "Please specify what you would like to order (e.g., 'I would like to order pizza')."
        elif "status" in processed_message:
            if active_order:
                response = handle_order_status(active_order)
            else:
                response = "You haven't placed an order yet. Please order something first."
        else:
            response = "I'm sorry, I don't understand. Please ask about the menu, order, or status."

        return render(request, 'chatbot/index.html', {'response': response})

    return render(request, 'chatbot/index.html')

def handle_order_status(active_order):
    status_messages = {
        'preparing': "Your food is being prepared.",
        'packing': "Your food is being packed.",
        'out_for_delivery': "Your food is out for delivery!",
        'delivered': "Your food has been delivered. Enjoy your meal!"
    }

    if active_order.status in status_messages:
        response = status_messages[active_order.status]
        # Update status for the next stage
        if active_order.status == 'preparing':
            active_order.status = 'packing'
        elif active_order.status == 'packing':
            active_order.status = 'out_for_delivery'
        elif active_order.status == 'out_for_delivery':
            active_order.status = 'delivered'
        active_order.save()
    else:
        response = "Unexpected order status."

    return response
