from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE, Avg


class Ideas(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    user = models.ForeignKey(User, on_delete=CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']


RATE_CHOICES = [
    (1, '1 - Mauvais'),
    (2, '2 - Moyen'),
    (3, '3 - OK'),
    (4, '4 - Bon'),
    (5, '5 - Excellent'),
]


class Comments(models.Model):
    idea = models.ForeignKey(Ideas, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
