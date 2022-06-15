from django.contrib import admin
from .models import Line, Station, Pharmacylocation, Hospital, Pharmacy, Convenience

# Register your models here.

class StationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Line)
admin.site.register(Station, StationAdmin)
admin.site.register(Pharmacylocation)
admin.site.register(Hospital)
admin.site.register(Pharmacy) 
admin.site.register(Convenience)