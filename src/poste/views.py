from django.views.generic import DateDetailView


class PostDateDetailView(DateDetailView):
    def get_template_names(self):
        template_list = super(PostDateDetailView, self).get_template_names()

        # Adding default post detail template
        template_list.append('poste/post_detail.html')

        return template_list
