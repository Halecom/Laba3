from django import forms

from apps.chat import models


class CreateChatForm(forms.ModelForm):
    class Meta:
        model = models.Chat
        fields = ("name",)


class CreateMessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ("nickname", "text")
