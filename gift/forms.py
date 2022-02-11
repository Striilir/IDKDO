from django import forms

from .models import Comments, RATE_CHOICES, Ideas


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = '__all__'
        exclude = {
            'date_added', 'user'
        }


class CommentForm(forms.ModelForm):
    text = forms.CharField(label='Texte', widget=forms.Textarea(
        attrs={'class': 'Small Focused textarea', 'placeholder': 'Commentaires'}))
    rate = forms.ChoiceField(label='Note', choices=RATE_CHOICES,
                             widget=forms.Select(attrs={'class': 'select is-small'}), required=True)

    class Meta:
        model = Comments
        fields = ('text', 'rate')
