from django.db import models

# Create your models here.
class CallScript(models.Model):
    idtag = models.CharField(max_length=255)
    html = models.TextField() 
    
    def __unicode__(self):
        return self.idtag
