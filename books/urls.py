from django.urls import path
from . import views

urlpatterns = [
	path('books', views.home, name='books-home'),
]