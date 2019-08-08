from django.urls import path
from . import views

urlpatterns = [
    #Create
    path('new/', views.new),
    path('create/', views.create),

    #Read
    path('', views.index),

    #Answer
    path('<int:question_id>/answers/create/', views.answer_create),
    path('answers/<int:question_id>/detail/', views.answer_detail),
]
