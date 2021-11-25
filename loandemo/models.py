from django.db import models

class UssdUser(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=14, unique=True)
    date_of_birth = models.DateField()
    transaction_pin = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.name

    

class LoanModel(models.Model):
    
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    plan = models.CharField(max_length=20)
    user = models.ForeignKey(UssdUser, on_delete=models.CASCADE, null=True, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}'s loan details"