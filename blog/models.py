from PIL import Image

from django.db import models
from django.conf import settings
from authentication.models import User
# Create your models here.


class Photo(models.Model):
    IMAGE_MAX_SIZE=(400,400)
    image=models.ImageField("media courant", upload_to=None, height_field=None, width_field=None, max_length=None)
    uploader=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    caption=models.CharField( max_length=128,blank=True)
    date_created=models.DateTimeField( auto_now=False, auto_now_add=True)
    def resize(self):
        img=Image.open(self.image)
        img.thumbnail(self.IMAGE_MAX_SIZE)
        img.save(self.image.path)
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        self.resize()
class Blog(models.Model):
    photo=models.ForeignKey(Photo ,null=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=128)
    content=models.CharField(max_length=5000)
    starred=models.BooleanField(default=False)
    date_created=models.DateTimeField( auto_now=False, auto_now_add=True)
    world_count=models.IntegerField(null=True)
    contributors=models.ManyToManyField("authentication.User",through='interBlogUser',related_name='contributions')
    
    def _get_world_count(self):
        content=self.content.strip()
        self.world_count=content.count(' ')+1
        print("le resultat veritable est "+str(self.world_count))
    
    def save(self,*args, **kwargs):
        self._get_world_count()
        super().save(*args, **kwargs)
class interBlogUser(models.Model):
    contributors=models.ForeignKey(User, on_delete=models.CASCADE)
    blog=models.ForeignKey("blog.Blog",  on_delete=models.CASCADE)
    participation=models.CharField(null=True, max_length=50)
    class Meta:
        unique_together=('contributors','blog')
