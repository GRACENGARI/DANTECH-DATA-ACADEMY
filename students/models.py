from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='students/')
    
    def __str__(self):
        return self.name
    
class  Organazations(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='organazations',default='image')
    

    def __str__(self):
        return self.name
    
    
class Pictures(models.Model):
    name = models.CharField(max_length=100)
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='pictures/')
    url = models.CharField(max_length=200)


    def __str__(self):
        return self.name
    
class Forms(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.name
    

