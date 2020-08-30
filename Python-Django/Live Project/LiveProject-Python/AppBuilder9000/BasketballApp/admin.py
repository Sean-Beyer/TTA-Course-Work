from django.contrib import admin
from .models import CreateContact
from .models import Schedule

# Register your models here.
admin.site.register(CreateContact)
admin.site.register(Schedule)