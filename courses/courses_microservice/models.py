from django.db import models
from django.utils.text import slugify

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Properly define the instructor field
    instructor = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    duration = models.IntegerField()  # Duration in hours
    level = models.CharField(max_length=50)  # Beginner, Intermediate, Advanced
    # e.g., Programming, Data Science, etc.
    category = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)  # Rating out of 5
    # image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    enrollment_count = models.IntegerField(
        default=0)  # Number of students enrolled
    # Unique slug for the course URL
    slug = models.SlugField(default="", blank=True,
                            max_length=255, unique=True)

    def save(self, *args, **kwargs):
        # Custom save method to handle slug creation
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.instructor} rating: {self.rating}"
