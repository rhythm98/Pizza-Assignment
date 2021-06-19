from djongo import models


class Topping_item(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Size_item(models.Model):
    name = models.CharField(max_length=100,primary_key=True)



class Pizza(models.Model):


    Type = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    Toppings = models.ArrayField(model_container=Topping_item)












