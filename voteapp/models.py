from django.db import models

class People(models.Model):
    MyName = models.CharField(max_length=100) 
    GoodPerson = models.CharField(max_length=100)  
    comment = models.TextField() 
    
    def __str__(self):
        return f"素敵さん{self.GoodPerson}"