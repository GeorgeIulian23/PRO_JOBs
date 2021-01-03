from django.db import models
from aplicatie2.models import Companies
# Create your models here.

title = (('programator', 'programator'), ('medic', 'medic'),
         ('Pilot de instalare în industrii chimice','Pilot de instalare în industrii chimice '),
         ('Operator ','Operator '),('Pilot instalare industria','Pilot instalare industria',),('Asistant','Asistant'),('Agent','Agent'))

class Jobs(models.Model):

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    url = models.CharField(max_length=25)
    titlu = models.CharField(max_length=40,choices=title)
    description = models.CharField(max_length=100)
    how_to_apply  = models.TextField()
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} - {self.type} - {self.titlu}"
