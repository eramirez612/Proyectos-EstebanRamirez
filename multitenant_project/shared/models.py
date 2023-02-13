from django.db import models
from tenant_schemas.models import TenantMixiN
# Create your models here.

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    on_trial = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    auto_create_schema = True
    
class Language(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    
