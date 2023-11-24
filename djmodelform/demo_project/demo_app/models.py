from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.
class Master(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True,verbose_name="Active")
    created_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    class Meta:
        abstract = True
        ordering = ['-isactive']

class State(Master):
    statename = models.CharField(max_length=200, unique=True,verbose_name="State")

    class Meta:
        verbose_name_plural = "States"
        ordering = ['-isactive']

    def __str__(self):
        return self.statename
    
class District(Master):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    districtname = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Districts"

    def __str__(self):
        return self.districtname


class Branch(Master):
    branch = models.CharField(max_length=200)
    branch_code = models.CharField(max_length=50, unique=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, limit_choices_to={"isactive": True})
    district = ChainedForeignKey(District, chained_field="state", chained_model_field="state")


    class Meta:
        verbose_name_plural = "Branches"
        ordering = ("state", "district")

    def __str__(self):
        return self.branch
    
class Course(Master):
    course_code = models.CharField(max_length=20)
    course_university = models.CharField(max_length=100)
    course_instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.course_code
PROJECT_CHOICES = [
    ("Mini Project", "Mini Project"),
    ("Main Project", "Main Project"),
    ("Live Project", "Live Project"),
]
class Student(models.Model):
    name = models.CharField(max_length=220)
    image = models.ImageField(upload_to='images/', verbose_name="Photo")
    project_Type = models.CharField(
        max_length=20,
        choices=PROJECT_CHOICES,
        default='1'
    )
    courses = models.ManyToManyField(Course, related_name='courses')
