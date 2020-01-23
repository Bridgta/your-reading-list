from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('readings/', views.readings_index, name='index'),
    path('readings/<int:reading_id>/', views.readings_detail, name='detail'),
    path('readings/create/', views.ReadingCreate.as_view(), name='readings_create'),
    path('readings/<int:pk>/update/', views.ReadingUpdate.as_view(), name='readings_update'),
    path('readings/<int:pk>/delete/', views.ReadingDelete.as_view(), name='readings_delete'),
    path('readings/<int:reading_id>/add_read/', views.add_read, name='add_read'),
    path('readings/<int:reading_id>/assoc_note/<int:note_id>/', views.assoc_note, name='assoc_note'),
    path('readings/<int:reading_id>/unassoc_note/<int:note_id>/', views.unassoc_note,name='unassoc_note'),
    path('notes/', views.NoteList.as_view(), name='notes_index'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='notes_detail'),
    path('notes/create/', views.NoteCreate.as_view(), name='notes_create'),
    path('notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='notes_update'),
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='notes_delete'),
]