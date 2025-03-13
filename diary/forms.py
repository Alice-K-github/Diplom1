from django import forms
from diary.models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'content', 'media']

    def __init__(self, *args, **kwargs):
        # Подключение стилизации полей формы
        super(RecordForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите заголовок',
            'style': 'background-color: #FAEBD7; height:50px',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите текст',
            'style': 'background-color: #FAEBD7'
        })

        self.fields['media'].widget.attrs.update({
            'class': 'form-control',
            'style': 'background-color: #FAEBD7'
        })
