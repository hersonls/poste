from django.views.generic import DetailView
from django.views.generic import DateDetailView
from django.views.generic.base import TemplateResponseMixin


class BaseTemplateMixin(TemplateResponseMixin):
    def get_template_names(self):
        template_list = super(BaseTemplateMixin, self).get_template_names()

        # Adding default post detail template
        template_list.append('poste/post_detail.html')

        return template_list


class PostDetailView(BaseTemplateMixin, DetailView):
    pass


class PostDateDetailView(BaseTemplateMixin, DateDetailView):
    pass
