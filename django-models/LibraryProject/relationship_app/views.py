from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test



# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


class UserRegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'relationship_app/register.html', {'form': form})

def role_required(role):
    def decorator(view_func):
        return user_passes_test(lambda u: u.is_authenticated and hasattr(u, 'userprofile') and u.userprofile.role == role)(view_func)
    return decorator

@role_required('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@role_required('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@role_required('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
