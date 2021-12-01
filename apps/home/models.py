

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Lesson(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    what_youll_learn = models.TextField()
    pre_requisites = models.TextField()
    content = models.TextField()
    question = models.TextField()
    solution = models.TextField()
    input = models.TextField()
    output = models.TextField()
    has_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title
