from django.contrib import admin
from blog.models import blogdata

# Register your models here.
class blogdataAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'date',)
  list_display_links = ('id', 'title',)

admin.site.register(blogdata, blogdataAdmin)
