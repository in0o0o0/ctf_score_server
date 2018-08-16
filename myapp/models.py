from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=40)

    CATEGORY_CHOICES =  (
        ('web', 'web'),
        ('pwn', 'pwn'),
        ('Forensics', 'Forensics'),
        ('Cryptography', 'Cryptography'),
        ('misc', 'misc'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    point = models.IntegerField()

    description = models.TextField()

    attachment = models.FileField(upload_to='admin',blank='true')
