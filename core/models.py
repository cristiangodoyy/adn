from django.db import models

# Create your models here.


class Dna(models.Model):
    dna = models.TextField(primary_key=True)
    is_mutant = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Adn'
        verbose_name_plural = 'Adns'
        db_table = 'core_adn'
