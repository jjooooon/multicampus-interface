from django.contrib import admin
from .models import Algorithm

class AlgorithmAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Algorithm, AlgorithmAdmin)
