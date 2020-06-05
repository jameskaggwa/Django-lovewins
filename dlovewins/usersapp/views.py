from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# messages.debug, messages.info, messages.success, messages.warning, messages.error

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'usersapp/register.html', {'form': form})
