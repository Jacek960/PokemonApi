from django.db import models

class Pokemon(models.Model):
    pok_name = models.CharField(max_length=200)
    pok_height = models.IntegerField()
    pok_weight = models.IntegerField()
    pok_img_url = models.URLField()
    pok_abilitys = models.ManyToManyField("Ability")

    def __str__(self):
        return self.pok_name


class Ability(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)