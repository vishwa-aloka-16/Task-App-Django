from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm,UserRegisterForm
from django.contrib import messages
# Create your views here.


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)      
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('app-profile')
    else:
        form = UserUpdateForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'users/profile.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Now you are able to log in.')
            return redirect('app-login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})