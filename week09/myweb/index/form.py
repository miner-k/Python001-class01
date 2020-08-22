from django import forms
class LoginForm(forms.Form):
    username = forms.CharField()  # 创建标准的输入框
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)  # widget设置格式,min_length设置最小长度

class SigninForm(forms.Form):
    username = forms.CharField()  # 创建标准的输入框
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)  # widget设置格式,min_length设置最小长度

