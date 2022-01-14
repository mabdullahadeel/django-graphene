from django.db import models


class ManufacturerBaseCountry(models.Model):
    CATEGORY_NAME_CHOICES = (
        ('None', 'none'),
        ('German', 'german'),
        ('Japanese', 'japanese'),
        ('American', 'american'),
    )
    
    name = models.CharField(max_length=30, choices=CATEGORY_NAME_CHOICES, unique=True)

    class Meta:
        verbose_name = 'Manufacturer Country'
        verbose_name_plural = 'Manufacturer Country'

    def __str__(self):
        return self.name
    


class Manufacturer(models.Model):
  name = models.CharField(max_length=30, unique=True)
  logo_url = models.CharField(max_length=256)
  base_country = models.ForeignKey(to=ManufacturerBaseCountry, related_name='base_country', on_delete=models.CASCADE)

  def __str__(self):
    return self.name


class Car(models.Model):
    CAR_COLOR_OPTONS = (
        ('white', 'white'),
        ('red', 'red'),
        ('green', 'green'),
        ('grey', 'grey'),
        ('grey', 'grey'),
        ('blue', 'blue'),
        ('orange', 'orange'),
        ('orange', 'orange'),
        ('black', 'black'),
    )

    name = models.CharField(max_length=256)
    features_description = models.TextField()
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=models.CASCADE, related_name="manufacturer")
    color = models.CharField(max_length=256, choices=CAR_COLOR_OPTONS)

    def __str__(self):
        return self.name