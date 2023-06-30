from django.urls import path,include

from . import views

app_name = 'group'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recruit_id>/', views.detail, name='detail'),
    path('answer/create/<int:recruit_id>/', views.answer_create, name='answer_create'),
    path('recruit/create/', views.recruit_create, name='recruit_create'),
    path('recruit/modify/<int:recruit_id>/', views.recruit_modify, name='recruit_modify'),
    path('recruit/delete/<int:recruit_id>/', views.recruit_delete, name='recruit_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    path('comment/recruit/question/<int:recruit_id>/', views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', views.comment_delete_question, name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>/', views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', views.comment_delete_answer, name='comment_delete_answer'),
]