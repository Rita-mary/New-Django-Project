from django.shortcuts import redirect, render
from .models import Profile
from .forms import NewUserForm
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid:
            user = form.save
        return redirect('/app1/index')
    form = NewUserForm()
    context = {'form' : form}
    return render(request , 'users/register.html', context)
