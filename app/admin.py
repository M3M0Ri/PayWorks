from django.contrib import admin
from app.models import JobPost


class JobAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title", "date", "salary",)
    list_filter = ("date", "salary", "expiry")
    search_fields = ["title", "description"]
    search_help_text = "You can Search Any thing you want"


admin.site.register(JobPost, JobAdmin)
