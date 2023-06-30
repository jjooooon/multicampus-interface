from django.contrib import admin
from . import models


@admin.register(models.Ranker)
class RankingAdmin(admin.ModelAdmin):
    pass
