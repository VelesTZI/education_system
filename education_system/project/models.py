from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    author_creathor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='product',
    )

    name_product = models.CharField(max_length=255)
    start_date_time_product = models.DateTimeField()
    price_product = models.DecimalField(decimal_places=2, max_digits=10)


    def __str__(self) -> str:
        return self.name_product


class Lesson(models.Model):
    lesson_product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='lesson_product',
    )

    neme_lesson = models.CharField(max_length=255)
    video_link = models.URLField()


class Group(models.Model):
    group_members = models.ManyToManyField(
        User,
        related_name='group_members',
    )
    min_count_users = models.PositiveBigIntegerField()
    max_count_users = models.PositiveBigIntegerField()
    group_product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='group_product',
    )
    def get_category(self): 
        return ",".join([str(p) for p in self.group_members.all()])
    

class AcessProduct(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
    )
    