from django.contrib import admin
from django.contrib.admin import register
from django.utils.safestring import mark_safe

from blogs.models import Post, Category


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@register(Post)
class PostAdmin(admin.ModelAdmin):
    autocomplete_fields = ['owner']
    list_display = ['title', 'image_html', 'owner']
    list_filter = ['title']
    search_fields = ['title']

    def owner_name(self, post):
        return '{0} {1}'.format(post.owner.first_name, post.owner.last_name)

    owner_name.admin_order_field = 'owner__first_name'
    owner_name.short_description = 'Nombre del Owner'

    def image_html(self, post):
        return mark_safe(
            '<img src="{0}" alt="{1}" title="{2}" width="100">'.format(post.image.url, post.title, post.title))

    image_html.short_description = 'Image'
    image_html.admin_order_field = 'image'

    fieldsets = [
        [None, {
            'fields': ['title', 'category', 'image', 'intro', 'post_body']
        }]
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        obj.save()


admin.site.site_header = 'Wordplease Admin'
admin.site.site_title = 'Wordplease Admin'
admin.site.index_title = 'Dashboard'
