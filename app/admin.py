from django.contrib import admin
from app.models import JobPost


class JobAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title", "date", "salary",)
    list_filter = ("date", "salary", "expiry")
    search_fields = ["title", "description"]
    search_help_text = "You can Search Any thing you want"
    #fields = (("title", "description"), "expiry")
    #exclude = ("title", )
    fieldsets = (
        ("Basic information", {
        "fields": ("title", "description")
         }),
        ("More information", {
            "classes":("collapse", ),
            "fields": (("salary", "expiry"), "slug")
        }),
    )


admin.site.register(JobPost, JobAdmin)
