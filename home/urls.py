from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('book_list', views.book_list, name='book_list'),
    path('book', views.book, name='book'),
    path('search', views.search_books, name='search'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('comment', views.comment, name='comment'),
    path('borrow_book', views.borrow_book, name='borrow_book'),
    path('team', views.team, name='team'),
    path('terms', views.terms, name='terms'),
    path('help', views.help, name='help'),
    path('FAQs', views.FAQs, name='FAQs'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('error', views.error, name='error'),
    path('sort', views.sort_books, name='sort'),
    path('login', views.u_login, name='login'),
    path('register', views.u_register, name='register'),
]
