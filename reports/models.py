from django.db import models

# Create your models here.
class category(models.Model):
    ROAD_SAFETY = "road_safety"
    STREET_LIGHTING = "street_lighting"
    CRIME_SECURITY = "crime_security"
    ENVIRONMENTAL = "environmental"
    PEDESTRIAN_SAFETY = "pedestrian_safety"
    SCHOOL_SAFETY = "school_safety"
    PROPERTY_HAZARD = "property_hazard"
    OTHER = "other"

    CATEGORY_CHOICES = [
        (ROAD_SAFETY, "Road Safety"),
        (STREET_LIGHTING, "Street Lighting"),
        (CRIME_SECURITY, "Crime / Security"),
        (ENVIRONMENTAL, "Environmental"),
        (PEDESTRIAN_SAFETY, "Pedestrian Safety"),
        (SCHOOL_SAFETY, "School Safety"),
        (PROPERTY_HAZARD, "Property Hazard"),
        (OTHER, "Other"),
    ]

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name