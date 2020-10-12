from django.contrib import admin
from . import models

@admin.register(models.Words)
class WordsAdmin(admin.ModelAdmin):
    list_display = ["id", "word", "hans"]