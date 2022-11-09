from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12,null=True)
    city = models.CharField(max_length=20,null=True)
    zip = models.CharField(max_length=6,null=True)
    state = models.CharField(max_length=48, null=True)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name