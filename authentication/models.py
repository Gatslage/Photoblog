from django.db import models
from django.contrib.auth.models import AbstractUser,Group


class User(AbstractUser):

    CREATOR='CREATOR'
    SUSCRIBER='SUSCRIBER'
    ROLES_CHOICES=(
        (CREATOR,'Createur'),
        (SUSCRIBER,'Abonné')
    )
    follows=models.ManyToManyField('self',symmetrical=False,limit_choices_to={'role':CREATOR})
    profil=models.ImageField(verbose_name="photo de profil", upload_to=None, height_field=None, width_field=None, max_length=None)
    role=models.CharField(verbose_name="role de l'utilisateur",choices=ROLES_CHOICES, max_length=50)
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        if self.role=='CREATOR':
            creator=Group.objects.get(name='creators')
            creator.user_set.add(self)
            creator.save()
        elif self.role=='SUSCRIBER':
            suscriber=Group.objects.get(name='suscribers')
            suscriber.user_set.add(self)
            suscriber.save()
# Create your models here.
