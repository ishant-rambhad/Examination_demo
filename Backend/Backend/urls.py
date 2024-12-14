# backend/backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/chatbot/', include('Chatbot.urls')),
    path('api/students/', include('students.urls')),
    # path('institutes/', include('institutes.urls')),
]