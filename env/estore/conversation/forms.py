from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)

class InChatMessageForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Type your message...',
            'class': 'form-group',}))

    class Meta:
        model = ConversationMessage
        fields = ('content',)