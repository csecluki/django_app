from django.db import models
from django.utils.text import slugify

from users.models import User


class Task(models.Model):

    objects = None

    class Meta:
        unique_together = ('user', 'name', 'slug')

    class TaskStatus(models.IntegerChoices):
        TODO = 0, 'To do'
        IN_PROGRESS = 1, 'In progress'
        DONE = 2, 'Done'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    status = models.SmallIntegerField(choices=TaskStatus.choices, default=0)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Task, self).save(*args, **kwargs)

    def change_status(self):
        if self.status < 2:
            self.status += 1
            self.save()
