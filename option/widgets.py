import json

from django.template import loader
from django import forms


class JsonEditorWidget(forms.Textarea):

    def __init__(self, *args, **kwargs):
        self.template = kwargs.pop('template', 'widgets/json_editor.html')
        super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        template = loader.get_template(self.template)
        context = self.get_context(name, value, attrs)
        return template.render(context)

    class Media:
        css = {
            "all": (
                "codemirror/lib/codemirror.css",
                "codemirror/addon/lint/lint.css",
                "codemirror/theme/rubyblue.css",
            )
        }
        js = (
            'codemirror/lib/codemirror.js',
            'codemirror/mode/javascript/javascript.js',
            'codemirror/addon/lint/jsonlint.js',
            "codemirror/addon/lint/lint.js",
            "codemirror/addon/lint/json-lint.js"
        )
