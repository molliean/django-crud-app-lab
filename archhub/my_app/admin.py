from django.contrib import admin

# Register your models here.
from .models import Place, Hours, Architect
admin.site.register(Place)
admin.site.register(Hours)
admin.site.register(Architect)