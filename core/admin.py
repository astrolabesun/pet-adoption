from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models, forms

# Register your models here.

class ApplicantAdmin(UserAdmin):
    model = models.Applicant
    add_form = forms.ApplicantCreationForm
    form = forms.ApplicantChangeForm

    list_display = ['email', 'username']

    fieldsets = (
        (None, {'fields': ('email', 'username', 'phone', 'address',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'username', 'phone', 'address', 'password1', 'password2',)}),
    )

    search_fields = ['email', 'username', 'phone', 'address']
    list_filter = ['is_staff']

admin.site.register(models.Applicant, ApplicantAdmin)
admin.site.register(models.Pet)
admin.site.register(models.AdoptionApplication)
