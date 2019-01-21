from django.db import models
from datetime import datetime

# realtors_realtor is going to be the table name. realtors = app name & realtor = classname
# The def __str__(self) is there so that the `name` is displayed in the admin page.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

