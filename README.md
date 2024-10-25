# Restaurant Chatbot

## Overview

The Restaurant Chatbot is a web application built with Django that simulates a conversational experience for customers looking to order food. It allows users to interact with a chatbot to inquire about the menu, place orders, and check the status of their orders.

## Features

- **Interactive Chat Interface**: Users can chat with the bot and receive responses based on their input.
- **Menu Inquiry**: Users can ask about available menu items.
- **Order Placement**: Users can place orders by specifying their desired food items.
- **Order Status Tracking**: Users can check the status of their orders as they progress through various stages (e.g., preparing, packing, out for delivery, delivered).

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (or specify any other database you used)
- **Natural Language Processing**: NLTK (for future enhancements)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/restaurant-chatbot.git
   cd restaurant-chatbot
   
2. Create and activate a virtual environment:
   python -m venv myenv
   myenv\Scripts\activate
   
3. Install the required packages:
   pip install -r requirements.txt
   
4. Download NLTK data:
   import nltk
   nltk.download('punkt')

5. Run the migrations (if using a database):
   python manage.py migrate

6. Start the development server:
   python manage.py runserver

7. Access the application by navigating to http://127.0.0.1:8000/ in your web browser.

**Usage**
Type your message in the input field and click the "Send" button to interact with the chatbot.
Use commands like "Hi", "Menu", or "Order [item]" to get responses from the bot.

**Future Enhancements**
Implementing more advanced NLP features using NLTK for a better user experience.
Adding user authentication to personalize interactions.
Expanding the menu and order management capabilities.

**Acknowledgments**
Thanks to the NLTK library for providing tools for natural language processing.
Special thanks to the Django community for their documentation and support.
   

