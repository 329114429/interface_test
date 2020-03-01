from django import forms

from .models import Topic, Entry


class TopicFrom(forms.ModelForm):
    """创建主题的表单"""

    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ' '}


class EntryForm(forms.ModelForm):
    """创建表单内容"""

    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ' '}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
