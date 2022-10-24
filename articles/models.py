import datetime

from django.db import models
from django.db.models import Q
from django.utils.text import slugify

from users.models import User


class Article(models.Model):

    class Meta:
        permissions = (
            ('publish_article', "Can publish article"),
        )

    class PublishStatus(models.IntegerChoices):
        HIDDEN = 0
        PUBLISHED = 1

    objects = None

    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=32, null=False, unique=True)
    author = models.ForeignKey(
        User,
        limit_choices_to=Q(is_staff=True) | Q(groups=(3,)),
        on_delete=models.CASCADE
    )
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, null=True)
    publish_date = models.DateTimeField(null=True)
    status = models.SmallIntegerField(choices=PublishStatus.choices, default=PublishStatus.HIDDEN)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    @property
    def like_counter(self):
        return self.likes.count()

    def get_lead(self):
        first_paragraph = self.split_content()[0]
        lead = first_paragraph[:1021] + '...'
        return lead

    def split_content(self):
        return str(self.content).split('\n')

    def publish(self):
        self.publish_date = datetime.datetime.now()
        self.status = self.PublishStatus.PUBLISHED
        self.save()


class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
