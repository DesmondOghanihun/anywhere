from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField(blank=True)  # Make message optional by adding `blank=True`
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contact from {self.name}'




class ICTTrainingRequest(models.Model):
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Request by {self.name} for {self.course}'





class ICTRequest(models.Model):
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Request by {self.name} for {self.course}'


