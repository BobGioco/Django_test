from django.shortcuts import render
from Project_app.forms import UserForm,UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

def user_login(request):
    if request.method=='POST':#if someone click submit button
        username=request.POST.get('username')#we use get because in login.html we use simple HTML and we called is 'username' and that's what we are getting
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)  #search for this user

        if user:#if the user is in database
            if user.is_active:#if user is active
                login(request,user)
                return HttpResponseRedirect(reverse('index'))#return to index.html
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print(f"Username: {username} and password {password}")
            return HttpResponse("Invalid login details!")
    else:#render login.html
        return render(request,'Project_app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("<h1>You are logged in , Nice!</h1>")

def index(request):
    return render(request,'Project_app/index.html')

def register(request):
    registered=False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()#save dirrectly to database
            user.set_password(user.password)#this goes to settings.py and hashes the password accordingly
            user.save()#save changes

            profile=profile_form.save(commit=False)#i don't want to commit to database yet, otherwise i can error because it may try to everwrite the user
            profile.user=user#this sets up  the on to one relationship (that's what we did in models.py)

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'Project_app/registration.html',{'user_form':user_form,
                                                        'profile_form':profile_form,
                                                        'registered':registered})
