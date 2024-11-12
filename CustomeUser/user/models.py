from django.utils import timezone
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomerUserManager(BaseUserManager):

    def creat_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user=self.mode(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extra_fields):

        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_superuser", True)
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user



class CustomUser(AbstractBaseUser,PermissionsMixin):

    email=models.EmailField(_("Email address"), unique=True)

    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    user_name=models.CharField(_("uder name"),max_length=15,unique=True,
                               help_text=("max length is 15-numbers and Letters"),
                               validators=[
                                   RegexValidator(
                                       regex=r'^[a-zA-Z]{3}\d{3}$',
                                       message="Enter a valid registration number in the format AbC123.",
                                       code="invalid_registration",
                                   )
                               ],
                               error_messages={
                                   'unique': _("A user with that username already exists."),
                               }

    )
    phone_number=models.CharField(_('mobile number'), unique=True, null=True, blank=True,max_length=20,
                                     validators=[
                                            RegexValidator(
                                                regex=r'^\+98[0-9]{10}$',
                                                message="Phone number must be entered in the format: '+989123456789'. Up to 10 digits allowed after the country code",

                                            )
                                    ],
                                     error_messages={
                                         'unique' : _("enter valid phone number")
                                     }
    )
    is_staff= models.BooleanField(_('is staff'),default=False,help_text=("Designates whether the user can log into this admin site. "))
    is_active=models.BooleanField(_('is active'),default=False,)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number","name","last_name"]

    objects=CustomerUserManager()


    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)


