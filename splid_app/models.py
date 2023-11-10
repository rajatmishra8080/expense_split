from django.db import models

# Create your models here.
class contact(models.Model):
    id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=25)
    phone=models.CharField(max_length=12)
    email=models.EmailField(max_length=50)
    def __str__(self):
        return self.fname
class expence(models.Model):
    expenseDate=models.DateField()
    expenseTitle=models.CharField(max_length=25)
    expenseAmount=models.DecimalField(max_digits=10, decimal_places=2,)
    expenseBy=models.CharField(max_length=100,)
    def __str__(self):
        return f"{self.expenseBy} - {self.expenseAmount}"
