from django.contrib import admin
from bitbilder.models import Bit

# Register your models here.
class BitAdmin(admin.ModelAdmin):
    fieldsets = [
            ("Dateien",                  {'fields': ['bit_image', 'bit_vector']}),
            ("Metadaten",                {'fields': ['bitname', 'author', 'creation_date', 'license']}),
            ("Reservierung",             {'fields': ['reserved', 'reserved_for']})
    ]

admin.site.register(Bit, BitAdmin)
