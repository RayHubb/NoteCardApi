from . import views
from django.urls import path

urlpatterns = [
    path('', views.CollectionList.as_view()),
    path('<int:collection_id>/notecards/', views.NoteCardDetail.as_view()),
]
