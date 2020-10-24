# 쟝고내에서 제공되는 form 기능을 사용하기위해 forms.py 만듬

from django import forms

class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required' : '제목을 입력해주세요.'
        },
        
            max_length=128, label="제목")
    contents = forms.CharField(
        error_messages={
            'required' : '내용을 입력해주세요.'
        },
            label="내용", widget=forms.Textarea)
