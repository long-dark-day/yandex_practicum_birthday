from django.contrib import admin

from .models import Birthday


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )
    list_editable = (
        'birthday',
    )
    search_fields = ('first_name',)
    list_display_links = ('first_name',)

@admin.register(Birthday)
class MyAdminPanel(admin.ModelAdmin):
    pass