from django.db import models
from django.contrib.auth.models import User
# Create your models here.


Gender_Choices=[
    ('Male','Male'),
    ('Female','Female')
]

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    username=models.CharField(max_length=32)
    Name=models.CharField(max_length=64)
    dob=models.DateField()
    gender=models.CharField(max_length=32,choices=Gender_Choices)
    photo=models.FileField(upload_to='documents/')
    status=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_id}'


