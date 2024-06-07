from django.db import models

# class vic_event(models.Model):  
#     your_name=models.CharField(max_length=100,default='')
#     event_name = models.CharField(max_length=100)
#     event_date = models.CharField(max_length=100)
    
#     email=models.CharField(max_length=100,default='')
#     state=models.CharField(max_length=100,default='')
#     city=models.CharField(max_length=100,default='')
    
#     event_description = models.TextField()
#     guests=models.CharField(max_length=100,default='')
#     event_category = models.CharField(max_length=100)


# but hamene build in use kara hai in djnago auth
class vic_register(models.Model):
    fiest_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2=models.CharField(max_length=50)


class vic_contact(models.Model):  
    name=models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100)


# event/models.py



class vic_event(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()  # Ensure this is DateField or DateTimeField
    event_description = models.TextField()
    event_category = models.CharField(max_length=100)
    guests = models.IntegerField()
    email = models.EmailField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    your_name = models.CharField(max_length=100)

    def __str__(self):
        return self.event_name
