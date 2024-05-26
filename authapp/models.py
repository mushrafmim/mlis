from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class LaboratoryStaff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    role = models.CharField(max_length=50, default='Laboratory Staff')
    status = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
