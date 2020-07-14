from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from PIL import Image
# Create your models here.


class UpcomingEvent(models.Model):
    month = models.DateField()
    description = models.CharField(max_length=80)
    time = models.TimeField()
    location = models.CharField(default='41 okiki str grandmate', max_length=100)
    image=models.ImageField(default='event.jpg', upload_to='eventpic')

    def __str__(self):
        return self.description


class NextBigEvent(models.Model):
    event = models.CharField(default='Next Event', max_length=80)
    date = models.DateField()

    def __str__(self):
        return self.event


class slide(models.Model):
    biblequote = models.CharField(max_length=60)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=70)
    date = models.DateField()
    The_time = models.TimeField()

    def __str__(self):
        return self.title


class LatestSermon(models.Model):
    title = models.CharField(max_length=60)
    by = models.CharField(max_length=150)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='sermon.jpg', upload_to='sermons_pic')
    word = RichTextField()
   

    def __str__(self):
        return self.title

    
    def save(self, *args,**kwargs):
        super(LatestSermon, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 400:
            output_size=(400,500)
            img.thumbnail(output_size)
            img.save(self.image.path)

  


class donation(models.Model):
    image = models.ImageField(default='donate.jpg', upload_to='donationproject_pic')
    For_What = models.CharField(default='church building', max_length=40)
    brief_description = models.CharField(max_length=70)

    def __str__(self):
        return self.For_What


class address(models.Model):
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = "Addresses"


# phone number
class phone_number(models.Model):
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.phone_number}'


# email
class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Ministries(models.Model):
    Ministry = models.CharField(max_length=40)
    description = models.TextField(max_length=200)
    image = models.ImageField(
        default='defaultdepart.jpg', upload_to='departments_pic')

    def __str__(self):
        return self.Ministry

    class Meta:
        verbose_name_plural = "Ministries"


class pastors(models.Model):
    name = models.CharField(max_length=40)
    role = models.CharField(max_length=20)
    image = models.ImageField(default='pastor.jpg', upload_to='pastors_pic')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pastors"

# this is for the blog session

class video(models.Model):
    video = models.FileField(default='defaultvideo.jpg', upload_to='videos')
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title





class CustomerInfo(models.Model):
    firstname= models.CharField(max_length  = 150)
    lastname= models.CharField(max_length  = 150)
    email= models.EmailField()
    phonenumber = models.CharField(max_length= 20)
    amount=models.IntegerField(default=1000)
    state = models.CharField(default='enter state',max_length = 150)


    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        verbose_name_plural = "Donators"


class prayer(models.Model):
    title=models.CharField(max_length=500)
    prayers=RichTextField()
    date_posted=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "prayer points"


class breadcrumb(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Breadcrumb"