from django.db import models

# Create your models here.
from django.db import models

class ContactMap(models.Model):
    map_image = models.ImageField(upload_to='map/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Contact Map"




from django.db import models

class LearningEnvironment(models.Model):
    image = models.ImageField(upload_to='learning/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Environment {self.id}"