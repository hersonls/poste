from django import forms


class CKEditorWidget(forms.Textarea):
    class Media:
        css = {
            "all": ("poste/css/ckeditor_widget.css", )
        }

        js = (
            'poste/js/libs/ckeditor/ckeditor.js',
            'poste/js/libs/ckeditor/styles.js',
            'poste/js/ckeditor_widget.js',
        )

    def __init__(self, attrs=None):
        default_attrs = {'class': 'dj_ckeditor'}
        if attrs:
            default_attrs.update(attrs)
        super(CKEditorWidget, self).__init__(default_attrs)
