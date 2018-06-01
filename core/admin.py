from django.contrib import admin
from .models import Dna


class AdnAdmin(admin.ModelAdmin):
    list_display = ('dna', 'is_mutant')

admin.site.register(Dna, AdnAdmin)
