from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserForm, UserProfileInfoForm
from django.urls import reverse_lazy ,reverse
from django.views import generic
from accounts.models import UserprofileInfo
from django.http import HttpResponseRedirect ,HttpResponse 
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)  # hash password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
            return HttpResponseRedirect(reverse('login'))
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'accounts/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })


def user_login(request):

    if request.method == 'POST' :

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(user= username,password= password)
        
        if user :
            if user.is_active :
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                HttpResponse('ACCOUNT NOT ACTIVE!')
        else:
            print('ACCOUNT DOSENT EXIST!')
    
    else:
        return render(request,'accounts/login.html')

@login_required 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
