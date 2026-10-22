from django.db import models

class ServiceCategoryChoices(models.TextChoices):

    PHOTOGRAPHY = 'Photography', 'Photography'
    DJ = 'DJ', 'DJ'
    VIDEOGRAPHY = 'Videography', 'Videography'
    DECORATION = 'Decoration', 'Decoration'