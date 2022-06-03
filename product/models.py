from django.db import models

# Create your models here.


class Drink(models.Model):
    class Meta:
        db_table = "drink"

    def __str__(self):
        return self.name

    # category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    # drink_category = models.ManyToManyField(Category)
    name = models.CharField(max_length=20, blank=False)
    ingredient = models.CharField(max_length=256)


class Category(models.Model):
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.category_name

    category_name = models.CharField(max_length=50)
    menu = models.ManyToManyField(Drink)
