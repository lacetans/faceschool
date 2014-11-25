from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class FSUser(models.Model):
    user = models.OneToOneField( User )
    course = models.CharField(max_length=10)
    classroom = models.CharField(max_length=10)
    def __unicode__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Soci.objects.get_or_create(user=instance)
        post_save.connect(create_user_profile, sender=User)


class Penalty(models.Model):
    user = models.ForeignKey( FSUser )
    permanent = models.BooleanField(default=False)
    end_date = models.DateTimeField(blank=True)
    channel = models.ForeignKey(blank=True)

class Post(models.Model):
    text = models.CharField(max_length=2000)
    pub_date  = models.DateTimeField()
    edit_date = models.DateTimeField(blank=True)
    user = models.ForeignKey( FSUser )
    #image = 

class Like(models.Model):
    post = models.ForeignKey( Post )
    user = models.ForeignKey( FSUser )
    date = models.DateTimeField()

class Dislike(models.Model):
    post = models.ForeignKey( Post )
    user = models.ForeignKey( FSUser )
    date = models.DateTimeField()

class Complaint(models.Model):
    post = models.ForeignKey( Post )
    user = models.ForeignKey( FSUser )
    date = models.DateTimeField()

class Reputation(models.Model):
    post = models.ForeignKey( Post )
    user = models.ForeignKey( FSUser )
    date = models.DateTimeField()
    points = models.IntegerField()

class Channel(models.Model):
    responsible = models.ForeignKey( FSUser )
    topic = models.CharField(max_length=200)
    description = models.TextField()
    def __unicode__(self):
        return self.topic

class UserChannel(models.Model):
    user = models.ForeignKey( FSUser )
    channel = models.ForeignKey( Channel )

