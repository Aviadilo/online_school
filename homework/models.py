from django.db import models
from user_auth.models import User
from hometask.models import Hometask


class Homework(models.Model):
    homework_owner = models.ForeignKey(
        User,
        verbose_name="Homework owner",
        related_name="owner_homeworks",
        on_delete=models.CASCADE
    )

    hometask = models.ForeignKey(
        Hometask,
        verbose_name="Task",
        related_name="made_homeworks_for_task",
        on_delete=models.CASCADE
    )

    homework_file = models.FileField(
        upload_to='uploads/homeworks/%Y/%m/%d'
    )

    mark = models.PositiveSmallIntegerField(
        verbose_name="Mark",
        null=True
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
        return "Homework of {} to task № {}".format(self.homework_owner, self.hometask.id)

    class Meta:
        verbose_name = "Homework"
        verbose_name_plural = "Homeworks"
        ordering = ['-created_date', 'homework_owner']


class Comment(models.Model):
    comment_owner = models.ForeignKey(
        User,
        verbose_name="Comment owner",
        related_name="owner_comments",
        on_delete=models.CASCADE
    )

    homework = models.ForeignKey(
        "Homework",
        verbose_name="Homework",
        related_name="homework_comments",
        on_delete=models.CASCADE
    )

    comment = models.TextField(
        verbose_name="Comment"
    )

    created_date = models.DateTimeField(
        verbose_name="Created",
        auto_now=False,
        auto_now_add=True
    )

    def __str__(self):
        return "Comment of user {} to homework №{}".format(self.comment_owner, self.homework.id)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['-created_date', 'homework']
