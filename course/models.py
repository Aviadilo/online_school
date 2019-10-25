from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Course(models.Model):
    course_owner = models.ForeignKey(
        User,
        verbose_name="Course owner",
        on_delete=models.CASCADE
    )

    name = models.CharField(
        verbose_name='Course name',
        max_length=128
    )

    teachers = models.ManyToManyField(
        User,
        verbose_name='Teachers',
        related_name='course_teachers',
        null=True,
        blank=True
    )

    students = models.ManyToManyField(
        User,
        verbose_name='Students',
        related_name='course_students',
        null=True,
        blank=True
    )

    created_date = models.DateTimeField(
        verbose_name="Created",
        auto_now=False,
        auto_now_add=True
    )

    updated_date = models.DateTimeField(
        verbose_name="Updated",
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return "Course {}".format(self.name)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['-created_date', 'name']
