from django.db import models


class Services(models.Model):
    name = models.CharField(max_length=100,blank=True)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='Icons/',null=True)


    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='Gallery/',null=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=150,blank=True)
    tagline = models.CharField(max_length=200,blank=True)
    img = models.ImageField(upload_to='Blog/',null=True)
    desc = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name    
    
class Testimonials(models.Model):
    name = models.CharField(max_length=100,blank=True)
    desc = models.TextField(blank=True)
    

  