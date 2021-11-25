from django.contrib import admin
from .models import UssdUser, LoanModel

# Register your models here.

class UssdUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'date_of_birth']

class LoanModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'balance', 'plan', 'user']

admin.site.register(UssdUser, UssdUserAdmin)
admin.site.register(LoanModel, LoanModelAdmin)
