from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
from rest_framework.exceptions import ValidationError


class Group(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    max_attempts = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1)])
    passing_score = models.FloatField(blank=True, null=True,validators=[MinValueValidator(0),MaxValueValidator(100)])
    is_active = models.BooleanField(default=True)

    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    groups = models.ManyToManyField(Group)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="questions/",
        blank=True,
        null=True
    )

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    def save(self, *args, **kwargs):
        if not self.text and not self.image:
            raise ValidationError("Please provide text or image.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.text or f"Question {self.id}"


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers"
    )
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["question"],
                condition=models.Q(is_correct=True),
                name="answer_is_correct"
            )
        ]


class Submission(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.quiz.title}"


class SubmissionAnswer(models.Model):
    submission = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE
    )

    is_correct = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.is_correct = self.answer.is_correct
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SubmissionAnswer {self.id}"