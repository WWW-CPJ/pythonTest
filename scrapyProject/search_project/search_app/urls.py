from django.urls import path
from .views import search_view
from .chat_views import chatbot_api

urlpatterns = [
    path('', search_view, name='search_view'),
    path('chatbot-api/', chatbot_api, name='chatbot_api'),
]