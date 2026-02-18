from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diary_entries')
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mood = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name_plural = 'Diary Entries'
    
    def __str__(self):
        return f"{self.title} - {self.date}"
