from django.db import models
from lecture.models import Lecture


class Hometask(models.Model):
    lecture = models.ForeignKey(
        Lecture,
        verbose_name="Lecture theme",
        related_name="lecture_tasks",
        on_delete=models.CASCADE
    )

    task_body = models.TextField(
        verbose_name="Task"
    )

    possible_max_mark = models.PositiveSmallIntegerField(
        verbose_name="Max mark for the task"
    )

    created_date = models.DateTimeField(
        verbose_name="Created",
        auto_now=False,
        auto_now_add=True
    )

    def __str__(self):
        return "Task №{} to lecture {}".format(self.id, self.lecture.theme)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['-created_date', 'lecture']
