from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate

from accounts.forms import UserCreateForm
from accounts.models import User


# Create your views here.
@login_required(login_url='/accounts/login/')
def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def Login(request):
    if request.user.is_authenticated:
        return redirect('chat:index')
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("chat:index")
        else:
            context = {
                "username": username,
            }
            return render(request, "accounts/login.html", context)
    else:
        return render(request, 'accounts/login.html', {})



def signup(request):
    if request.user.is_authenticated:
        return redirect('chat:index')
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password2'])
            user.save()
            return redirect('accounts:login')
    else:
        form = UserCreateForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
