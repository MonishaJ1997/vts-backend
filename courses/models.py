from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):

    CATEGORY_CHOICES = [
        ('Development', 'Development'),
        ('Design', 'Design'),
        ('Data', 'Data'),
        ('Emerging Tech', 'Emerging Tech'),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    duration = models.CharField(max_length=100)
    level = models.CharField(max_length=100, default="Beginner to Advanced")
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



from django.db import models


class Coursedetails(models.Model):
    title = models.CharField(max_length=200)

    # Right side video thumbnail image
    video_thumbnail = models.ImageField(upload_to="courses/video_thumbnails/")

    # Optional: video file (if needed later)
    intro_video = models.FileField(upload_to="courses/videos/", blank=True, null=True)

    def __str__(self):
        return self.title


class CourseTechnology(models.Model):
    course = models.ForeignKey(
        Coursedetails,
        on_delete=models.CASCADE,
        related_name="technologies"
    )

    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="courses/technologies/")

    def __str__(self):
        return f"{self.course.title} - {self.name}"



from django.db import models

class PaymentMethod(models.Model):
    METHOD_CHOICES = [
        ("upi", "UPI"),
        ("netbanking", "Net Banking"),
        ("card", "Card"),
    ]

    title = models.CharField(max_length=50)
    method_type = models.CharField(max_length=20, choices=METHOD_CHOICES)
    icon = models.ImageField(upload_to="payment_icons/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.method_type})"