from django.db import models
from django.urls import reverse

# Create your models here.
class movielist(models.Model):
    movie_img= models.ImageField(upload_to="gallery/",null=True)
    movie_name=models.CharField(max_length=200)
    movie_lang=models.CharField(max_length=200)
    movie_cat=models.CharField(max_length=200)
    movie_mlink=models.CharField(max_length=200)
    movie_tlink=models.CharField(max_length=200)
    movie_like=models.CharField(max_length=200)
    movie_byindustry=models.CharField(max_length=200)
    movie_home=models.CharField(max_length=200)
    def get_absolute_url(self):
        return reverse('catone',args=[self.movie_cat])
    class Meta:
        db_table = 'movielist'
    

