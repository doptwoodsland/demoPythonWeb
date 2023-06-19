from django.contrib import admin

from .models import Post, Choise, Question

# Register your models here.

# class PostAdmin(admin.ModelAdmin):
#     list_display_date = ['title','date']
#     list_age = ['age','integer']

admin.site.register(Post)
admin.site.register(Choise)
admin.site.register(Question)
# admin.site.register(PostAdmin)

