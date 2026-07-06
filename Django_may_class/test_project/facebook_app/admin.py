from django.contrib import admin
from .models import Account

# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email')
    list_filter = ('gender',)
    search_fields = ('firstname', 'lastname', 'email')