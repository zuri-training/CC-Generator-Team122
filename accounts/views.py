from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm, LoginForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Tutorial, TutorialPreference
from django.contrib.auth.decorators import login_required


#NOTE user authentication not yet completed...password not checked
def signup_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request, "signup.html", {"form":form})


def login(request):
    if request.method == 'POST':
        login = LoginForm(request.POST)

        #Note cleaned_data is only available when you use is_valid
        if log_form.is_valid():
            email = log_form.cleaned_data["email"]
            password = log_form.cleaned_data["password"]

            #check if user in database
            user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index.html')
        else:
            messages.info(request, 'wrong username or password')
            return redirect('index')
    form = LoginForm()
    return render(request, 'login.html', {'form':form})


def logout_req(request):
    auth.logout(request)
    return redirect('landingpage.html')

@login_required
def tutorialpreference(request, postid, userpreference):
    if request.method == "POST":
        eachtutorial= get_object_or_404(Tutorial, id=tutorialid)
        obj= "valueobj="
        try:
            obj= TutorialPreference.object.get(user= request.user, post= eachtutorial)
            valueobj= obj.value #value of user preference
            valueobj= int(valueobj)
            tutorialpreference= int(tutorialpreference)
            if valueobj != tutorialpreference:
                obj.delete()

                tpref= TutorialPreference()
                tpref.user= request.user
                tpref.tutorial= eachpost
                tpref.value= tutorialpreference

                if tutorialpreference == 1 and valueobj != 1:
                    eachtutorial.likes += 1
                    eachtutorial.dislikes -= 1
                elif tutorialpreference == 2 and valueobj != 2:
                    eachtutorial.dislikes += 1
                    eachtutorial.likes -= 1

                tpref.save()
                eachtutorial.save()
                context= {'eachtutorial':eachtutorial, 'tutorialid':tutorialid}
                return  render(request, 'landingpage.html', context )
        except TutorialPreference.DoesNotExist:
            tpref= TutorialPreference()
            tpref.user= request.user
            tpref.tutorial= eachtutorial
            tpref.value= tutorialpreference
            tutorialpreference= int(tutorialpreference)
            if tutorialpreference == 1:
                eachtutorial.likes += 1
            elif tutorialpreference == 2:
                eachtutorial.dislikes += 1
            tpref.save()
            eachtutorial.save()
            context= {'eachtutorial':eachtutorial, 'tutorialid':tutorialid}
            return render (request, 'landingpage.html', context)

    else:
        eachtutorial= get_object_or_404(Tutorial, id=tutorialid)
        context= {'eachtutorial':eachtutorial, 'tutorialid':tutorialid}
        return render(request, 'landingpage.html', context)








