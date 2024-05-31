from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .signals import user_registered
from .form import CustomUserCreationForm

@login_required
def home(request):
    return render(request, "home.html",{"form":form})
# Create your views here.
def authView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST or None)  # Use your custom user creation form
        if form.is_valid():
            user = form.save()
            user_registered.send(sender=None, user=user)
            return redirect('home')  # Redirect to home or any other page after successful signup
    else:
        form = CustomUserCreationForm()  # Use your custom user creation form
    return render(request, "registration/signup.html", {"form": form})