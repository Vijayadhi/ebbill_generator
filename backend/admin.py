from django.contrib import admin

from backend.models import CustomUser, MonthlyEbBill

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(MonthlyEbBill)
