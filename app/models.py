from django.db import models

class DogProduct(models.Model):
    name = models.TextField()
    product_type = models.TextField()
    dog_size = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()

class Purchase(models.Model):
    dog_product = models.ForeignKey(DogProduct, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField()

class DogTag(models.Model):
    owner_name = models.TextField()
    dog_name = models.TextField()
    dog_birthday = models.DateField()
    dog_color = models.TextField()
    

