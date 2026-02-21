from django.db import models

# Create your models here.
# app/models.py
from django.db import models

class AboutImage(models.Model):
    title = models.CharField(max_length=100, default="About VTS Image")
    image = models.ImageField(upload_to="about/")

    def __str__(self):
        return self.title



# app/models.py
from django.db import models

class MissionVision(models.Model):
    TYPE_CHOICES = (
        ("mission", "Mission"),
        ("vision", "Vision"),
    )

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    icon = models.ImageField(upload_to="mission_vision/")

    def __str__(self):
        return self.type



from django.db import models

class EcosystemSection(models.Model):
    title = models.CharField(max_length=200)
    center_text = models.CharField(max_length=200)
    left_image = models.ImageField(upload_to="ecosystem/")

    def __str__(self):
        return self.title


class EcosystemItem(models.Model):
    section = models.ForeignKey(EcosystemSection, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="ecosystem/logos/")
    point1 = models.CharField(max_length=255)
    point2 = models.CharField(max_length=255)
    site_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


from django.db import models

class ValueCard(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='value_icons/')  # icon image
    bullets = models.JSONField()  # store bullet points as list

    def __str__(self):
        return self.title




from django.db import models

class TrainingStep(models.Model):
    title = models.CharField(max_length=100)  # Example: "Entry & Counseling"
    description = models.TextField()
    image = models.ImageField(upload_to='training_steps/')
    order = models.PositiveIntegerField(default=1)  # to sort steps
    journey_name = models.CharField(max_length=100, default="Your Training Journey")  # optional grouping

    def __str__(self):
        return f"{self.journey_name} - {self.title}"




        from django.db import models

class WhoCanJoin(models.Model):
    COLOR_CHOICES = [
        ('orange', 'Orange'),
        ('purple', 'Purple'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='who_can_join/')
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='orange')

    def __str__(self):
        return self.name
    


    # models.py
from django.db import models

class CareerPerson(models.Model):
    name = models.CharField(max_length=100)  # optional, if you want
    image = models.ImageField(upload_to='career_person/')

    def __str__(self):
        return self.name or "Career Person"