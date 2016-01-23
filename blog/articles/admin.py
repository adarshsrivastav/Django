from django.contrib import admin
from .models import Artical,Comment

# Register your models here.

#class ChoiceInline(admin.TabularInline):
#    model = Comment
#    extra = 0

class ArticalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title','alt_title','author','category','star_image','optional_image','body','likes']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
 #   inlines = [ChoiceInline]


admin.site.register(Artical,ArticalAdmin)
admin.site.register(Comment)