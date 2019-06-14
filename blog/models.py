from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')



class Post(models.Model):

    #limit input with dropdown
    STATUS_CHOICES =(
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    #blogpost's title
    title = models.CharField(max_length = 250)

    #url builder (???)
    slug = models.SlugField(
        max_length = 250,
        #adds publish date to url
        unique_for_date = 'publish',
    )

    #foreign key. one user, many posts
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'blog_post',
        )

    #to store the content
    body = models.TextField()

    #storing the important dates
    publish = models.DateTimeField(default = timezone.now)

    created = models.DateTimeField(auto_now_add = True)

    #last update only
    updated = models.DateTimeField(auto_now = True)

    status = models.CharField(
        max_length = 10,
        #use dropdown
        choices = STATUS_CHOICES,
        default = 'draft'
    )

    #default manager
    objects = models.Manager()

    #custom manager
    published = PublishedManager()

    #order posts latest first
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
