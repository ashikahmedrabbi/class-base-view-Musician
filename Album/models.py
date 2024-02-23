from django.db import models
from musician.models import Musician



# Create your models here.
class Album(models.Model):
        Album_Name= models.CharField(max_length=100)
        Musician = models.ForeignKey(Musician, on_delete=models.CASCADE) #
        
        Album_release_date= models.DateField()
        Album_Rating =( 
            ("1", "1"), 
            ("2", "2"), 
            ("3", "3"), 
            ("4", "4"), 
            ("5", "5"), 
        ) 
        Rating=models.CharField(max_length=5, choices=Album_Rating,default=0)


    
        def __str__(self):
            return self.Album_Name
