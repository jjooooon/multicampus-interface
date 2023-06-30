from django import forms
from group.models import Recruit, Applicant, Comment


class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit  # 사용할 모델
        fields = ['select', 'subject', 'content', 'personnel' ]

        labels = {
            'select' : '현재 공고중인 공모전',
            'subject': '제목',
            'content': '내용',
            'personnel' : '모집인원',
        }

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }