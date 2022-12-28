from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Vegitable(models.Model):
    name = models.CharField(max_length=30)
    disc = models.TextField()
    price = models.FloatField(default=0)
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

class reviews(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Vegitable,on_delete=models.CASCADE)
    review = models.TextField()
    posted_on = models.DateField(default=timezone.now())

    def __str__(self):
        return f"{self.user}"

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Vegitable, on_delete=models.CASCADE)
    quntity = models.IntegerField(default=1)
    price = models.FloatField(default=1)
    ordered_on = models.DateField(default=timezone.now())

    def __str__(self):
        return f"{self.item}"



