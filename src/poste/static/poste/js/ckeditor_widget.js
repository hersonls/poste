//
// CKEditor default configurations
//


!function($, window, document, undefined){
    $(document).ready(function() {
        ckeditor_config = {
            width: '80%',
            skin: 'moono',
            language: "pt-br",
            toolbar :[
                ['Bold','Italic', 'Strike', 'Link', 'Unlink', 'NumberedList', 'BulletedList', 'Indent', 'Source']
            ]
        };

        $('textarea').each(function() {
            CKEDITOR.replace($(this).attr('id'), ckeditor_config);
        });
    });
}(django.jQuery || window.ender, window, document);
