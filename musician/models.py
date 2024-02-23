
from django.db import models
# Create your models here.
class Musician(models.Model):
    First_Name = models.CharField(max_length=15)
    Last_Name = models.CharField(max_length=15)
    Email = models.EmailField()
    phone_no = models.CharField(max_length=12)
    InstrumentType =( 
        ("1","Guitar"),
        ("2","Piano"),
        ("3","Drums"),
        ("4","Violin"),
        ("5","Trumpet"),
    ) 
    Instrument_Type=models.CharField(max_length=1, choices=InstrumentType, default=0)
    
    
    
    def __str__(self):
        return self.First_Name