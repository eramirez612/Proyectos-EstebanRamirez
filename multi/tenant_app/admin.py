from django.contrib import admin
from tenant_app.models import Sweet
# Register your models here.

@admin.register(Sweet)
class SweetAdmin(admin.ModelAdmin):
    list_display = ('name',)
    