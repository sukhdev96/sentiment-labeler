from django.contrib import admin

# Register your models here.

from .models import Post, Label
from import_export.admin import ImportExportModelAdmin


class PostAdmin(ImportExportModelAdmin):
    list_display = ('id','source','content','no_of_labels')

class LabelAdmin(ImportExportModelAdmin):
    list_display = ('id','post_ID','labeler','sentiment','timestamp')

admin.site.register(Post, PostAdmin)
admin.site.register(Label, LabelAdmin)