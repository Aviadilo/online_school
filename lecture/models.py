from django.db import models
from course.models import Course
from user_auth.models import User


class Lecture(models.Model):
    lecture_owner = models.ForeignKey(
        User,
        verbose_name="Lecture owner",
        related_name='owner_lectures',
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        verbose_name="Course name",
        related_name="course_lectures",
        on_delete=models.CASCADE
    )

    theme = models.CharField(
        verbose_name="Lecture theme",
        max_length=128
    )

    lecture_file = models.FileField(
        upload_to='uploads/lectures/%Y/%m/%d'
    )

    created_date = models.DateTimeField(
        verbose_name="Created",
        auto_now=False,
        auto_now_add=True
    )

    def __str__(self):
        return "Lecture {}".format(self.theme)

    class Meta:
        verbose_name = "Lecture"
        verbose_name_plural = "Lectures"
        ordering = ['-created_date', 'theme']
