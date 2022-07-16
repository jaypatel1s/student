from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.


class CustomUser(AbstractUser):

    USER(
        (1,'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT')

    )
    user_type = modeLs.Charfield(choices =USER)
    profile =pic