from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    technologies = models.CharField(max_length=500, help_text="Comma-separated list, e.g. Python, Django, React")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def tech_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"[{'Read' if self.is_read else 'New'}] {self.subject} - {self.name}"
