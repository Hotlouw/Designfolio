from django.db import models
from django.contrib.auth.models import User

class Library(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(null = True, blank = True, upload_to='images/')
    coding = models.TextField()
    details = models.TextField()
    category = models.ForeignKey(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class OtherLibrary(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name
        
class Other(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(null = True, blank = True, upload_to='images/')
    details = models.TextField()
    category = models.ForeignKey(OtherLibrary, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Email(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.sender

class Certification(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    Institution = models.CharField(max_length=255)
    certificate = models.ImageField(null = True, blank = True, upload_to='images/')
    syllabus = models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateField()
    article = models.TextField()
    signed = models.CharField(max_length=255)
    category = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
            return self.name



  
class UserProfile(models.Model):
    username = models.CharField(max_length=50, default = "*")
    password = models.CharField(max_length=50, default="*")

    def __str__(self):
        return self.username          
    
    