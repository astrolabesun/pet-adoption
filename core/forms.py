from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from . import models

class ApplicantCreationForm(UserCreationForm):
    class Meta:
        model = models.Applicant
        fields = ('email', 'username', 'phone', 'address',)


class ApplicantChangeForm(UserChangeForm):
    class Meta:
        model = models.Applicant
        fields = ('email', 'username', 'phone', 'address',)


class PetForm(ModelForm):
    class Meta:
        model = models.Pet
        fields = ('name', 'age', 'sex', 'animal_type', 'portrait', 'biography',)


class AdoptionApplicationForm(ModelForm):
    class Meta:
        model = models.AdoptionApplication
        fields = ('applicant', 'pet',)
