from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django_extensions.db.models import TimeStampedModel

# Create your models here.

class ApplicantManager(BaseUserManager):
    def create_user(self, email, username, phone, address, password=None):
        if not email:
            raise ValueError('Email is required!')
        user = Applicant(
            email=self.normalize_email(email), 
            username=username, 
            phone=phone,
            address=address
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, address, password=None):
        superuser = self.create_user(
            email=email,
            username=username,
            phone=phone,
            address=address,
            password=password
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using=self._db)
        return superuser



class Applicant(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=200, verbose_name='full name', unique=False)
    address = models.CharField(max_length=500)
    phone = models.PositiveBigIntegerField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone', 'address']
    objects = ApplicantManager()

    def __str__(self) -> str:
        return f'{self.email}, {self.username}'



class Pet(TimeStampedModel, models.Model):
    DOG = 'DOG'
    CAT = 'CAT'
    BIRD = 'BIRD'
    REPTILE = 'REPTILE'
    OTHER = 'OTHER'
    ANIMAL_TYPE = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (BIRD, 'Bird'),
        (REPTILE, 'Reptile'),
        (OTHER, 'Other')
    )
    MALE = 'M'
    FEMALE = 'F'
    SEX = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    name = models.CharField(max_length=100)
    animal_type = models.TextField(verbose_name='type of animal', choices=ANIMAL_TYPE, default=OTHER)
    age = models.IntegerField(verbose_name='age (in years)')
    sex = models.TextField(choices=SEX, default=MALE)
    portrait = models.ImageField(upload_to='images/', default='images/undraw_no_data_re_kwbl.svg', blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    is_adopted = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}, {self.animal_type}'



class AdoptionApplication(TimeStampedModel, models.Model):
    UNDER_REVIEW = 'U'
    INTERVIEW = 'I'
    APPROVED = 'A'
    DENIED = 'D'
    WITHDRAWN = 'W'
    APPLICATION_STATUS = (
        (UNDER_REVIEW, 'Under Review'),
        (INTERVIEW, 'Interview'),
        (WITHDRAWN, 'Withdrawn'),
        (DENIED, 'Denied'),
        (APPROVED, 'Approved')
    )
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    status = models.TextField(choices=APPLICATION_STATUS, default=UNDER_REVIEW)

    class Meta:
        permissions = [
            ('can_withdraw', 'the user can withdraw the application.'),
            ('can_approve', 'the user can set the application status to interview, approve, or deny.')
        ]

    def __str__(self) -> str:
        return f'{self.applicant} application for {self.pet}'
