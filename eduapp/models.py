from django.db import models
from django.contrib.auth.models import User


   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    phone_code = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    dob = models.DateField(max_length=255)
    gender = models.CharField(max_length=25)
    location_id = models.CharField(max_length=255)
    national_status = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.username


class events(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name 
    
class classes(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name 
    
class venues(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name 
    
class Category(models.Model):
    name = models.CharField(max_length=100)    
    def __str__(self):
        return self.name
    
class sports_classes(models.Model):
    name = models.CharField(max_length=100,null=True)
   
    
        
    def __str__(self):
        return self.name  
     
class Activity(models.Model):
    PRICING_CHOICES=(
    ("1", "Free"),
    ("2", "Paid")  
    )
    TICKET_CHOICES=(
    ("1", "Slots"),
    ("2", "Ticket")  
    )
    STATUS_CHOICES=(
    ("1", "Published"),
    ("2", "Unpublished")
    )
    activityname = models.CharField(max_length=255)
    activity_description = models.CharField(max_length=500)
    activity_image = models.ImageField(upload_to ='media')      
    CATEGORY_CHOICES = [(category.id, category.name) for category in Category.objects.all()]
   # activity_ids= models.IntegerField(choices=CATEGORY_CHOICES)
    pricing_types=models.CharField(choices=PRICING_CHOICES,max_length=50,null=True) 
    classes_names = models.ForeignKey(classes, on_delete=models.CASCADE,null=True)
    event_names= models.ForeignKey(events, on_delete=models.CASCADE,null=True)
    venue_names= models.ForeignKey(venues, on_delete=models.CASCADE,null=True)
    arabic_activityname=models.CharField(max_length=255,null=True)
    arabic_activitydescription=models.TextField(max_length=500,null=True)
    location=models.CharField(max_length=255,null=True)
    mail_id=models.CharField(max_length=255,null=True)
    mobile_no=models.CharField(max_length=255,null=True)
    prioriy=models.IntegerField(null=True)
    tickt_types= models.CharField(choices=TICKET_CHOICES,null=True,max_length=255,)
    created_at = models.DateTimeField(editable=False,null=True,max_length=255,auto_now_add=True)
    status_choice= models.CharField(choices=STATUS_CHOICES,null=True,max_length=255,)
   # start_date=models.DateField(null=True)
   # end_date=models.DateField(null=True)
    start_date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    end_date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    sports_classes = models.ForeignKey(sports_classes, on_delete=models.CASCADE,null=True,)
    
    start_time=models.TimeField(null=True)
    end_time=models.TimeField(null=True)  
    landmark=models.CharField(max_length=800,null=True)
    capacity=models.IntegerField(null=True,default=1)
    catagory=models.CharField(max_length=500,null=True)
    
    sports_type=(
        ("Basketball","Basketball"),
        ("Football","Football"),
        ("Swimming","Swimming"),
        ("Volley Ball","Volley Ball"),
        ('Music','Music')
    )
    select_sports=models.CharField(max_length=600,choices=sports_type,null=True)
    stundent_leval_type=(
        ('Beginner','Beginner'),
        ('InterMediate','InterMediate'),
        ('Expert','Expert')
    )
    stundent_leval=models.CharField(max_length=500,choices=stundent_leval_type,null=True)
    
    
    
    
class activity_tags(models.Model):
    activity_tags = models.CharField(max_length=255)