from django.conf.urls import patterns, url
from django.views.generic import DetailView
from django.views.generic import DayArchiveView
from django.views.generic import YearArchiveView
from django.views.generic import ArchiveIndexView
from django.views.generic import MonthArchiveView

from .models import Post
from .views import PostDetailView
from .views import PostDateDetailView


urlpatterns = patterns('',
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        DayArchiveView.as_view(queryset=Post.objects.all().select_subclasses(), date_field='pub_date', month_format='%m'),
        name='poste_post_archive_day'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        MonthArchiveView.as_view(
            queryset=Post.objects.all().select_subclasses(), date_field='pub_date', month_format='%m'),
        name='poste_post_archive_month'
    ),
    url(r'^(?P<year>\d{4})/$',
        YearArchiveView.as_view(queryset=Post.objects.all().select_subclasses(), date_field='pub_date', make_object_list=True),
        name='poste_post_archive_year'
    ),
    url(r'^(?P<year>\d+)/(?P<month>[-\w]+)/(?P<day>\d+)/(?P<slug>.*)/$',
        PostDateDetailView.as_view(queryset=Post.objects.all().select_subclasses(), month_format='%m', date_field="pub_date"),
        name="poste_post_date_detail"
    ),
    url(r'^(?P<slug>.*)/$',
        PostDetailView.as_view(
            queryset=Post.objects.all().select_subclasses()
        ),
        name='poste_post_detail'
    ),
    url(r'^$',
        ArchiveIndexView.as_view(
            queryset=Post.objects.all().select_subclasses(),
            date_field='pub_date'),
        name='poste_post_list'
    )
)
