from django.db import models
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(
        default=timezone.now)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

# class Comment(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.ForeignKey(Post)
#     comment_text = models.TextField()
#     comment_published_date = models.DateTimeField(
#         default=timezone.now, blank=True, null=True)
#
#     def __str__(self):
#         return "{0} {1}".format(self.comment_text, self.comment_published_date)