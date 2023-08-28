from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Book, BorrowedBook
from django.db.models import Q
from django.contrib import messages
from datetime import timedelta
#from django.http import HTTPResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def terms(request):
    return render(request, 'terms.html')

def team(request):
    return render(request, 'team.html')

def error(request):
    return render(request, 'error.html')

def help(request):
    return render(request, 'help.html')

def FAQs(request):
    return render(request, 'FAQs.html')

def contact(request):
    return render(request, 'contact.html')

def comment(request):
    return render(request, 'comment.html')

def error(request):
    return render(request, '404.html')

def testimonial(request):
    return render(request, 'testimonial.html')


def book_list(request):
    books = Book.objects.prefetch_related('collection').all()
    return render(request, 'book_list.html', {'books': books})


def book(request):
    books = Book.objects.prefetch_related('collection').all()
    return render(request, 'book_list2.html', {'books': books})


def u_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserRegistrationForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})



def u_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                
                # Check if the user is staff
                if user.is_staff:
                    # Redirect staff users to the admin page
                    return redirect('admin:index')  # You can customize this URL
                else:
                    # Redirect other users to the book_list page
                    return redirect('book_list')  # You should replace 'book_list' with your actual URL name
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})



def sort_books(request):
    sort_option=request.GET.get('sort_option', 'title')

    if sort_option=='title':
        books_order=Book.objects.order_by('title')
    elif sort_option=='arthor':
        books_order=Book.objects.order_by('arthor')
    elif sort_option=='category':
        books_order=Book.objects.prefetch_related('collection').order_by('collection')
    else:
        pass

    context={
        'books_order': books_order
    }

    return render(request, 'sort_books.html', context)


def search_books(request):
    query=request.GET.get('query', '')

    books = books.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query) | Q(collection__icontains=query)
    )

    context={
        'books': books
    }

    return render(request, 'search_books.html')


@login_required(login_url='login')
def borrow_book(request):
    book = get_object_or_404(Book)

    if book.available > 0:
        borrowed_book = BorrowedBook(book=book, borrower=request.user)
        borrowed_book.save()
        book.available -= 1
        book.save()

        messages.success(request, f"The book is ready for you '{book.title}'.")
        return redirect('book_list')
    else:
        messages.error(request, f"'{book.title}' is not available for borrowing.")
        return redirect('book_list')
