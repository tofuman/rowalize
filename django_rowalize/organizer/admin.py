from django.contrib import admin

from .models import Rower,Boat,CoxBox,Oars,Outing
# Register your models here.
admin.site.register(Rower)
admin.site.register(Boat)
admin.site.register(CoxBox)
admin.site.register(Oars)
admin.site.register(Outing)