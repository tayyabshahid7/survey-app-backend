from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Survey(models.Model):
    """A survey created by a user."""

    title = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Question(models.Model):
    """A question in a survey"""

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="questions")
    question_title = models.CharField(max_length=128)

    def __str__(self):
        return self.question_title


class Option(models.Model):
    """A multi-choice option available as a part of a survey question."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=128)

    def __str__(self):
        return self.text


class Answer(models.Model):
    """An answer a survey's questions."""

    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user_email = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(default=timezone.now)
