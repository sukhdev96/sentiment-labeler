from django.contrib import admin

# Register your models here.

from .models import Post, Label


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','source','content')

class LabelAdmin(admin.ModelAdmin):
    list_display = ('id','post_ID','content','labeler','sentiment')

admin.site.register(Post, PostAdmin)
admin.site.register(Label, LabelAdmin)