from django.contrib import admin
from .models import Contact, ICTTrainingRequest, ICTRequest

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'submitted_at')
    search_fields = ('name', 'email')

   

@admin.register(ICTTrainingRequest)
class ICTTrainingRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'email', 'phone', 'location', 'submitted_at')
    search_fields = ('name', 'course', 'email', 'phone', 'location')
    list_filter = ('submitted_at', 'course')
    readonly_fields = ('submitted_at',)


@admin.register(ICTRequest)
class ICTRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'email', 'phone', 'location', 'submitted_at')
    search_fields = ('name', 'course', 'email', 'phone', 'location')
    list_filter = ('submitted_at',)


