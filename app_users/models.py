from distutils.command.upload import upload
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
import os

def path_and_rename(instance, filename):
    upload_to = 'Imagens/'
    ext = filename.splite('-'[-1])
    if instance.user.username:
        filename = 'User_profile_Pictures/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)
# Create your models here.
USER_TYPES = (
    ('Professor', 'Professor'),
    ('Estudante', 'Estudante'),
   
)
 
class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.CharField(max_length=150, blank=True)

    imagem = models.ImageField(upload_to='path_and_rename', verbose_name='Imagens de Perfil', blank=True )


   

    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    def __str__(self):
        return self.user.username