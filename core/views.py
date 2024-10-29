from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms, models

# Create your views here.

def home(request):
    return render(request, 'index.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('user-profile', request.user.pk)

    context = {}
    if request.method == 'POST':
        user = authenticate(email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('user-profile', user.pk)
        else:
            context['error'] = 'Incorrect credentials. Please try again.'
    return render(request, 'login.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('user-profile', request.user.pk)

    context = {}
    form = forms.ApplicantCreationForm()
    if request.method == 'POST':
        form = forms.ApplicantCreationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('user-profile', user.pk)
        else:
            context['error'] = 'Invalid input. Please fill the form in correctly.'
    context['form'] = form
    return render(request, 'register.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def user_profile(request, pk):
    user = models.Applicant.objects.get(pk=pk)
    context = {'user': user}
    return render(request, 'user_profile.html', context)


@login_required(login_url='login')
def user_adoption_applications(request):
    adopt_applications = models.AdoptionApplication.objects.filter(applicant=request.user)
    context = {'adoption_applications': adopt_applications}
    return render(request, 'adopt_applications.html', context)


def pets_catalogue(request):
    pets = models.Pet.objects.all()
    context = {'pets': pets}
    return render(request, 'pets.html', context)


def pet_profile(request, pk):
    pet = models.Pet.objects.get(pk=pk)
    context = {'pet': pet}
    return render(request, 'pet_profile.html', context)


@login_required(login_url='login')
def adoption_application(request, pk):
    pet = models.Pet.objects.get(pk=pk)
    form = forms.AdoptionApplicationForm(initial={'applicant': request.user, 'pet': pet})
    context = {'pet': pet}
    if request.method == 'POST':
        form = forms.AdoptionApplicationForm(data={'applicant': request.user, 'pet': pet})
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('user-adoption-applications')
        else:
            context['error'] = 'Please fill out this form correctly.'
    context['form'] = form
    return render(request, 'apply.html', context)


@login_required(login_url='login')
def withdraw_application(request, pk):
    adoption_application = models.AdoptionApplication.objects.get(pk=pk)
    adoption_application.status = adoption_application.WITHDRAWN
    adoption_application.save()
    return redirect('user-adoption-applications')
