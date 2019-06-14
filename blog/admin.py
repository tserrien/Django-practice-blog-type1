from django.contrib import admin
from .models import Post
# Register your models here.

#original "default" layout and registration
#admin.site.register(Post)

@admin.register(Post) #decorator
class PostAdmin(admin.ModelAdmin):
    #what fields to display
    list_display = ('title', 'slug', 'author', 'publish', 'status')

    #filters for the admin surface
    list_filter = ('status', 'created', 'publish', 'author')

    #search fields for admin surface
    search_fields = ('title', 'body')

    #dafuq
    prepopulated_fields = {'slug': ('title',)}

    #replace author dropdown with id number input
    raw_id_fields = ('author',)

    #which date field is the base of filtering
    date_hierarchy = 'publish'

    #base of ordering
    ordering = ('status', 'publish')
