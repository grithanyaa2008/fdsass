from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

     
    CATEGORY_CHOICES = [
    ("Work", "Work"),
    ("Personal", "Personal"),
    ("Study", "Study"),
    ("Project", "Project"),
    ("Other", "Other"),
]
    TASK_TYPE_CHOICES = [
        ("Assignment", "Assignment"),
        ("Lab Work", "Lab Work"),
        ("Project", "Project"),
        ("Exam Preparation", "Exam Preparation"),
        ("Presentation", "Presentation"),
    ]

    STATUS_CHOICES = [
        ("Not Started", "Not Started"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    category = models.CharField(
    max_length=50,
    choices=CATEGORY_CHOICES,
    default="Other"
)

    task_type = models.CharField(
        max_length=30,
        choices=TASK_TYPE_CHOICES,
        default="Assignment"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Not Started"
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="Medium"
    )

    due_date = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title