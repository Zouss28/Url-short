from django.db import models
from django.conf import settings



# Create your models here.
class urlShort(models.Model):
    url = models.URLField(null=False)
    shortcode = models.CharField(unique=True, max_length=settings.MAX_LENGTH)
    
    def __str__(self) -> str:
        return str(self.url)
    
    
    @property
    def get_shortened_url(self):
        # Generate the dynamic shortened URL using the current domain and shortened code
        return f"http://shortify.com:8000/{self.shortcode}"
    
class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, urlShort):
            obj, created = self.get_or_create(kirr_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    kirr_url = models.OneToOneField(urlShort, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True) 
    timestamp = models.DateTimeField(auto_now_add=True) 
    
    objects = ClickEventManager()
    
    def __str__(self) -> str:
        return str(self.count)
