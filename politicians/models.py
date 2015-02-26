from django.db import models

# Create your models here.

class Politician(models.Model):
    name = models.CharField(max_length=255)
    party = models.ForeignKey("Party")
    group = models.ForeignKey("Group")
    sex = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female')))
    phone = models.PositiveIntegerField()
    shortcode = models.PositiveIntegerField()
    image = models.ImageField(upload_to="static/images/meps")
    email = models.EmailField()
    score = models.CharField(max_length=10, choices=(('positive', 'FOR'), ('uncertain', 'UNCERTAIN'), ('negative', 'AGAINST')))
    
    def __unicode__(self):
        return self.name

class Party(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name
        
class Quote(models.Model):
    who = models.ForeignKey("Politician")
    media = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField()
    quote = models.TextField()

    def __unicode__(self):
        return self.quote
