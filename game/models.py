from django.db import models
from django.utils import timezone
from django.conf import settings

class Image(models.Model):
    url = models.URLField()  # Store the image URL
    created_at = models.DateField(default=timezone.now)
    prompt = models.TextField(blank=True, null=True)
    has_been_described = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Image for {self.created_at}"

class Description(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='descriptions')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Description for {self.image.created_at}"
