from django.db import models

# Create your models here.

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    RegDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ExpenseDetails(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    amount = models.FloatField()
    category = models.CharField(max_length=50)
    Expensedate = models.DateField(null=True, blank=True)
    NoteDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.amount} - {self.category}" 