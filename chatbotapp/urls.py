from django.urls import path
from chatbotapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chatbot-response/', views.chatbot_response, name='chatbot_response'),
]
