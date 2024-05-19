from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    portfolio_item = models.ForeignKey(PortfolioItem, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)





class PhotoItem(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='photos/', verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    category = models.CharField(max_length=100, choices=[
        ('Nature', 'Nature'),
        ('Events', 'Events'),
        ('Portraits', 'Portraits'),
        ('Landscapes', 'Landscapes')
    ], verbose_name='Category')
    tags = models.CharField(max_length=100, verbose_name='Tags')
    location = models.CharField(max_length=200, blank=True, verbose_name='Location')
    public_visible = models.BooleanField(default=True, verbose_name='Publicly Visible')

    def __str__(self):
        return self.title


class Feedback(models.Model):
    photo_item = models.ForeignKey(PhotoItem, on_delete=models.CASCADE, related_name='feedback')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
