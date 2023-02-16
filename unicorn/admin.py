from django.contrib import admin

from unicorn.models import Unicorn

class UnicornAdmin(admin.ModelAdmin):
    model = Unicorn

admin.site.register(Unicorn, UnicornAdmin)
