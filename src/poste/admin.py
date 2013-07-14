from django.contrib import admin

from .models import Post
from .models import TextPost
from .models import ImagePost
from .models import Image
from .models import CodePost
from .models import QuotePost
from .models import LinkPost
from .models import ChatPost
from .models import AudioPost
from .models import VideoPost


class BasePostAdmin(admin.ModelAdmin):
    exclude = ('author', )

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class TextPostAdmin(BasePostAdmin):
    list_display = ('timestamp', 'pub_date', 'title')
    list_filter = ('timestamp', 'pub_date')
    search_fields = ('title', 'body')


class ImagePostAdmin(BasePostAdmin):
    list_display = ('timestamp', 'pub_date', 'title', 'image', 'is_external_image')
    list_filter = ('timestamp', 'pub_date')
    search_fields = ('title', )


class CodePostAdmin(BasePostAdmin):
    list_display = ('timestamp', 'pub_date', 'title', 'is_embed')
    list_filter = ('timestamp', 'pub_date')
    search_fields = ('title', 'code', 'embed')


class QuotePostAdmin(BasePostAdmin):
    list_display = ('timestamp', 'pub_date', 'title', 'quote', 'source')
    list_filter = ('timestamp', 'pub_date')
    search_fields = ('title', 'quote', 'source')


class LinkPostAdmin(BasePostAdmin):
    list_display = ('timestamp', 'pub_date', 'title', 'url', 'get_link_tag')
    list_filter = ('timestamp', 'pub_date')
    search_fields = ('title', 'url', 'caption')


class ChatPostAdmin(BasePostAdmin):
    list_display = ('timestamp', 'pub_date', 'title')
    list_filter = ('timestamp', 'pub_date')
    search_fields = ('title', 'url', 'chat')


class AudioPostAdmin(BasePostAdmin):
    list_display = ('timestamp', 'pub_date', 'title', 'is_external_audio')
    list_filter = ('timestamp', 'pub_date')
    search_fields = ('title', 'url')


class VideoPostAdmin(BasePostAdmin):
    list_display = ('timestamp', 'pub_date', 'title')
    list_filter = ('timestamp', 'pub_date')
    search_fields = ('title', 'url', 'embed')


admin.site.register(TextPost, TextPostAdmin)
admin.site.register(ImagePost, ImagePostAdmin)
admin.site.register(CodePost, CodePostAdmin)
admin.site.register(QuotePost, QuotePostAdmin)
admin.site.register(LinkPost, LinkPostAdmin)
admin.site.register(ChatPost, ChatPostAdmin)
admin.site.register(AudioPost, AudioPostAdmin)
admin.site.register(VideoPost, VideoPostAdmin)
