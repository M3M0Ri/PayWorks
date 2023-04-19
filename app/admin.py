from django.contrib import admin
from app.models import JobPost, Location, Author, Skills


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


admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)

