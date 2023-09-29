from django.db import models

class Frigo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nutrimcode = models.CharField(max_length=20) 

    def __str__(self):
        return self.nutrimcode