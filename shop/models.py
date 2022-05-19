from django.db import models


# Create your models here.
class Worker (models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.name


class Shop (models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=False)
    shop_name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговый точки'

    def __str__(self):
        return self.shop_name


class Visiting (models.Model):
    date = models.DateTimeField(auto_now_add=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
    
    def __str__(self):
        return str(self.shop)