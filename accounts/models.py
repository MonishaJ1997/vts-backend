from django.db import models

# Create your models here.
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="company_logo/")

    def __str__(self):
        return self.name
    



    from django.db import models

class WebsiteContent(models.Model):
  
    hero_image = models.ImageField(upload_to='hero/')

    title = models.CharField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AboutContent(models.Model):
    about_image = models.ImageField(upload_to="about/")
    title = models.CharField(max_length=200)
    description = models.TextField()
    established_year = models.CharField(max_length=10)
    established_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# website/models.py
from django.db import models

class WhyChooseUsSection(models.Model):
    title = models.CharField(max_length=200, default="Why Choose Us")
    description = models.TextField(blank=True, null=True)
    left_image = models.ImageField(upload_to="why_choose_us/left_images/", blank=True, null=True)

    def __str__(self):
        return self.title

class WhyChooseUsFeature(models.Model):
    section = models.ForeignKey(
        WhyChooseUsSection,
        on_delete=models.CASCADE,
        related_name="features"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to="why_choose_us/icons/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title





from django.db import models

class HowItWorksStep(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon_image = models.ImageField(upload_to='how_it_works/icons/', null=True, blank=True)
    step_number = models.IntegerField()
    card_bg_color = models.CharField(max_length=20, default="#F4D7A1")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"Step {self.step_number} - {self.title}"


class HowItWorksSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    student_image = models.ImageField(upload_to='how_it_works/student/')

    def __str__(self):
        return self.title


class FeaturedCourse(models.Model):
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    level = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="featured_courses/")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
    

    from django.db import models

class StudentProject(models.Model):
    title = models.CharField(max_length=200)
    student_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to="student_projects/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title



from django.db import models

class SuccessStory(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    image = models.ImageField(upload_to="success_stories/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name




from django.db import models

class FooterLogo(models.Model):
    logo = models.ImageField(upload_to='footer_logo/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Footer Logo"








from django.db import models

class EcosystemSectioned(models.Model):
    title = models.CharField(max_length=200)
    center_text = models.CharField(max_length=200)
    left_image = models.ImageField(upload_to="eco/")

    def __str__(self):
        return self.title


class EcosystemItemed(models.Model):
    section = models.ForeignKey(EcosystemSectioned, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="eco/logos/")
    point1 = models.CharField(max_length=255)
    
    site_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name




    # models.py
from django.db import models

class CareerMen(models.Model):
    name = models.CharField(max_length=100)  # optional, if you want
    image = models.ImageField(upload_to='career_men/')

    def __str__(self):
        return self.name or "Career Men"




class Storyrole(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StoryImage(models.Model):
    story = models.ForeignKey(
        Storyrole,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='success_story/')

    def __str__(self):
        return f"{self.story.name} Image"