from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='created_posts',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateField(auto_now_add=True, db_index=True)
    users_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_posts',
        blank=True,
    )

    @property
    def likes(self):
        return self.users_like.count()

    class Meta:
        ordering = ['created']