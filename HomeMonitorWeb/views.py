from django.shortcuts import render
from django.utils import timezone
from .models import Post, Data
from django.shortcuts import render, get_object_or_404
from .forms import SignUpForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})