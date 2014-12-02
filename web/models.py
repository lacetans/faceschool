from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class FSUser(models.Model):
    user = models.OneToOneField( User )
    # profile image
    # main image (portada)
    def __unicode__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = FSUser.objects.get_or_create(user=instance)
# link user to FSUser creation
post_save.connect(create_user_profile, sender=User)


class Channel(models.Model):
    responsible = models.ForeignKey( FSUser, related_name='responsible' )
    topic = models.CharField(max_length=200)
    description = models.TextField()
    users = models.ManyToManyField( FSUser )
    def __unicode__(self):
        return self.topic

class Post(models.Model):
    text = models.CharField(max_length=2000)
    pub_date  = models.DateTimeField()
    edit_date = models.DateTimeField(blank=True,null=True)
    user = models.ForeignKey( FSUser )
    channel = models.ForeignKey( Channel )
    #image = 
    def __unicode__(self):
        return "[%s] %s..." % (self.user.user.username,self.text[:20])

class Comment(Post):
    # same funcionality as Post with the related post
    related_post = models.ForeignKey( Post, related_name='related_post' )

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

class Penalty(models.Model):
    user = models.ForeignKey( FSUser )
    permanent = models.BooleanField(default=False)
    total = models.BooleanField(default=False)
    end_date = models.DateTimeField(blank=True)
    channel = models.ForeignKey( Channel, blank=True, null=True )
