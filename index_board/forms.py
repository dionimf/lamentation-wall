from django import forms
from parsley.decorators import parsleyfy

from index_board.models import *

@parsleyfy
class LamentationForm(forms.ModelForm):
    
    class Meta:
        fields = ('text',)
        model = LamentModel
        widgets = {
            'text': forms.Textarea(
                attrs={'style':
                       'height: 90px;',
                       'rows': None,
                       'class': 'form-control',
                       'placeholder': 'Deixe aqui sua lamentação'}),
        }

        parsley_extras = {'text':
                          { 'minlength': '5',
                            'error-message': 'Sua lamentação deve conter ao menos 5 caracteres.'}}

@parsleyfy
class CounselForm(forms.ModelForm):
    
    class Meta:
        fields = ('lament_id', 'text',)
        model = CounselModel
        widgets = {
            'lament_id': forms.HiddenInput(),
            'text': forms.Textarea(
                attrs={'style':
                       'width: 80%; display: inline;' +
                       'height: 100px;',
                       'rows': None,
                       'class': 'form-control',
                       'placeholder': 'Que conselho você quer dar?'}),
        }

        parsley_extras = { 'text': {
            'minlength': '5',
            'error-message': 'Seu conselho deve conter pelo menos 5 caracteres.',
        }, }
