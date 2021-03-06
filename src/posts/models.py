from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
from profiles.models import Profile


class Post(models.Model):
    """Model definition for Post."""

    # TODO: Define fields here
    content = models.TextField()
    image = models.ImageField(upload_to='posts', blank=True, validators=[
                              FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    liked = models.ManyToManyField(Profile, blank=True, related_name='likes')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        """Meta definition for Post."""
        ordering = ('-created',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return str(self.content[:20])

    def num_likes(self):
        return self.liked.all().count()

    def num_comments(self):
        return self.comment_set.all().count()

class Comment(models.Model):
    """Model definition for Comment."""

    # TODO: Define fields here
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Unicode representation of Comment."""
        return str(self.pk)


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    """Model definition for Like."""

    # TODO: Define fields here
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(max_length=8, choices=LIKE_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Like."""

        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        """Unicode representation of Like."""
        return f"(self.user)-(sef.post)-(self.value)"
