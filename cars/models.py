from django.db import models

class Manufacturer(models.Model):
  name = models.CharField(max_length=30, unique=True)
  logo_url = models.CharField(max_length=256)

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