from django.contrib import admin
from .models import NewSpace,NewSlot
# Register your models here.




class NewSlotAdmin(admin.StackedInline):
    model = NewSlot
    extra = 3

class NewSpaceAdmin(admin.ModelAdmin):

    inlines = [NewSlotAdmin]

admin.site.register(NewSpace , NewSpaceAdmin)
