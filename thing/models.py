from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ThingUser(models.Model):
    name = models.CharField(max_length=30
                            ,unique=True
                            ,blank=False
                            )
    description = models.CharField(max_length=120
                                   ,unique=False
                                   ,blank=True
                                    )
    quantity = models.IntegerField(unique=False
                                   ,validators=[MinValueValidator(0, message="Value must be at least 0."),
                                    MaxValueValidator(100, message="Value must be at most 100.")
                                   ]
                                   )



