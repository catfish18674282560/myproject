from django.contrib import admin
from . import models

@admin.register(models.Words)
class WordsAdmin(admin.ModelAdmin):
    list_display = ["id", "word", "hans", "is_recite"]
    actions = ['no_recite', "yes_recite"]

    def no_recite(self, request, queryset):
        queryset.update(is_recite=False)
    no_recite.short_description = "选择全部取消背诵"

    def yes_recite(self, request, queryset):
        queryset.update(is_recite=True)
    yes_recite.short_description = "选择全部开始背诵"