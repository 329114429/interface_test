import re
import hashlib

from django import forms
from django.forms import ValidationError

from .models import User

USERNAME_PATTERN = re.compile(r'\w{4,20}')


class RegisterForm(forms.ModelForm):
    """表单"""
    repassword = forms.CharField(min_length=8, max_length=20)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not USERNAME_PATTERN.fullmatch(username):
            raise ValidationError("用户名由字母,数字下划线组成, 4-20个字符")
        else:
            return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8 or len(password) > 20:
            raise ValidationError("密码长度8-20位")
        return to_md5_hex(self.cleaned_data['password'])

    def clear_repassword(self):
        repassword = to_md5_hex(self.cleaned_data['repassword'])
        if repassword != self.cleaned_data['password']:
            raise ValidationError("密码二次不一致")
        return repassword

    class Meta:
        model = User
        exclude = ('no', 'regdate')


def to_md5_hex(message):
    """加密"""
    return hashlib.md5(message.encode()).hexdigest()
