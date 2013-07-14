from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from .fields import UUIDField
from .fields import AutoSlugField
from .managers import InheritanceManager


def file_upload_path(instance, file_name):
    app_label, model_name = instance._meta.app_label, instance._meta.object_name.lower()

    return '{0}/{1}/{2}'.format(app_label, model_name, file_name)


class Post(models.Model):
    uuid = UUIDField(editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('author'))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_('timestamp'))
    title = models.CharField(max_length=4000, verbose_name=_('title'), blank=True)
    pub_date = models.DateTimeField(_('publication date'), blank=True, null=True)
    slug = AutoSlugField(prepopulate_from=('title', ), max_length=250, unique=True)

    objects = InheritanceManager()

    class Meta:
        ordering = ('-timestamp', )

    def __unicode__(self):
        if self.title:
            return self.title
        return _('{0} #{1}'.format(self._meta.object_name, self.pk))

    @models.permalink
    def get_absolute_url(self):
        args = [
            self.pub_date.strftime("%Y"),
            self.pub_date.strftime("%m"),
            self.pub_date.strftime("%d"),
            self.slug
        ]
        return ('poste_post_date_detail', args)

    def template(self):
        return '{0}/snippets/{1}_snippet.html'.format(self._meta.app_label, self._meta.object_name.lower())


class TextPost(Post):
    body = models.TextField(_('body'))

    class Meta:
        verbose_name = _('text post')
        verbose_name_plural = _('text posts')


class ImagePost(Post):
    image = models.ImageField(upload_to=file_upload_path, verbose_name=_('image'))
    url = models.URLField(_('external image URL'), blank=True)

    class Meta:
        verbose_name = _('image post')
        verbose_name_plural = _('image posts')

    def is_external_image(self):
        return (self.url != "")
    is_external_image.short_description = _('External Image')
    is_external_image.boolean = True


class Image(models.Model):
    image_post = models.ForeignKey(ImagePost, related_name='images_set', verbose_name=_('image post'))
    image = models.ImageField(upload_to=file_upload_path, verbose_name=_('image'))
    caption = models.CharField(max_length=4000, verbose_name=_('caption'))

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')


class CodePost(Post):
    embed = models.TextField(_('embed'), blank=True, null=True)
    code = models.TextField(_('code'), blank=True, null=True)

    class Meta:
        verbose_name = _('code post')
        verbose_name_plural = _('code posts')

    def is_embed(self):
        return (self.embed != "")
    is_embed.short_description = _('Embed Code')
    is_embed.boolean = True


class QuotePost(Post):
    quote = models.TextField(_('quote'))
    source = models.TextField(_('source'))

    class Meta:
        verbose_name = _('quote post')
        verbose_name_plural = _('quote posts')


class LinkPost(Post):
    url = models.URLField(_('URL'))
    caption = models.TextField(_('caption'), blank=True)

    class Meta:
        verbose_name = _('link post')
        verbose_name_plural = _('link posts')

    def get_link_tag(self):
        return '<a href="{0}" target="_blank">{1}</a>'.format(self.url, self.caption)
    get_link_tag.short_description = _('Visit')
    get_link_tag.allow_tags = True


class ChatPost(Post):
    chat = models.TextField(_('chat'))

    class Meta:
        verbose_name = _('chat post')
        verbose_name_plural = _('chat posts')


class AudioPost(Post):
    url = models.URLField(_('external audio URL'), blank=True)
    audio = models.FileField(upload_to='poste/autio/', blank=True)

    class Meta:
        verbose_name = _('audio post')
        verbose_name_plural = _('audio posts')

    def is_external_audio(self):
        return (self.url != "")
    is_external_audio.short_description = _('External Audio')
    is_external_audio.boolean = True


class VideoPost(Post):
    embed = models.TextField(_('embed'))

    class Meta:
        verbose_name = _('video post')
        verbose_name_plural = _('video posts')