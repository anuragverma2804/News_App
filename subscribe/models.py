from django.db import models


class Subscribe(models.Model):
    subs_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    headlines = models.BooleanField(default=True)
    bussiness = models.BooleanField(default=False)
    entertainment = models.BooleanField(default=False)
    health = models.BooleanField(default=False)
    science = models.BooleanField(default=False)
    technology = models.BooleanField(default=False)
    sports = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Contact_Us(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    desc=models.CharField(max_length=500)
    def __str__(self):
        return self.name
