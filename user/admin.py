from django.contrib import admin
from .models import CustomUser, InvestmentReport, Training, Evaluation
from .forms import CustomUserForm

class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserForm

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(InvestmentReport)
admin.site.register(Training)
admin.site.register(Evaluation)