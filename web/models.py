from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
from django.core.exceptions import ValidationError

class FSUser(models.Model):
    user = models.OneToOneField( User )
    upload_path = 'users_images'
    # profile image
    profile_image=models.ImageField(upload_to=upload_path+'/%Y/%m/%d', default='users_images/default_avatar.gif')
    # main image (portada)
    main_image = models.ImageField(upload_to=upload_path+'/%Y/%m/%d', default='users_images/default_main.jpg')
    
    def __unicode__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = FSUser.objects.get_or_create(user=instance)
# link user to FSUser creation
post_save.connect(create_user_profile, sender=User)

def validate_image(value):
    MAX_IMAGE_SIZE = 2621440 # 2.5MB in bits
    if value.size > MAX_IMAGE_SIZE:
        raise ValidationError(u'Image size must be less than 2.5MB.')

class Channel(models.Model):
    responsible = models.ForeignKey( FSUser, related_name='responsible' )
    topic = models.CharField(max_length=200)
    description = models.TextField()
    users = models.ManyToManyField( FSUser )
    def __unicode__(self):
        return "[%s] %s" % (self.responsible.user.username, self.topic)

class Post(models.Model):
    text = models.CharField(max_length=2000)
    pub_date  = models.DateTimeField()
    edit_date = models.DateTimeField(blank=True,null=True)
    user = models.ForeignKey( FSUser )
    channel = models.ForeignKey( Channel )
    upload_path= 'users_image'
    image = models.ImageField(upload_to=upload_path+'/%Y/%m/%d', blank=True, validators=[validate_image])
    
    def __unicode__(self):
        return "[%s] %s..." % (self.user.user.username,self.text[:30])
        
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.pub_date = datetime.datetime.today()
        self.edit_date = datetime.datetime.today()
        return super(Post, self).save(*args, **kwargs)

class Comment(Post):
    # same funcionality as Post with the related post
    related_post = models.ForeignKey( Post, related_name='related_post' )

class Like(models.Model):
    post = models.ForeignKey( Post )
    user = models.ForeignKey( FSUser )
    date = models.DateTimeField()
    def save(self, *args, **kwargs):
        self.date = datetime.datetime.today()
        return super(Like, self).save(*args, **kwargs)

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

class Badws(models.Model):
    texto = models.CharField(max_length = 30)
    def __unicode__(self):
        return self.texto

class Goodws(models.Model):
    texto = models.CharField(max_length = 30)
    def __unicode__(self):
        return self.texto

class Removebadws(models.Model):
    texto = models.CharField(max_length = 30)

class Removegoodws(models.Model):
    texto = models.CharField(max_length = 30)

class Badwsmasiva(models.Model):
    archivo = models.FileField(upload_to='import/')

class Goodwsmasiva(models.Model):
    archivo = models.FileField(upload_to='import/')
