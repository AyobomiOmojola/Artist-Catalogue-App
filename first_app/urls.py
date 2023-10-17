from django.urls import path
from . import views

app_name = 'first_app'     

urlpatterns = [
    path('',views.index,name='index'),

    path('albulm_form/',views.albulm_form,name='albulm_form'),

    path('musician_form/',views.musician_form,name='musician_form'),

    path('albulm_list/<int:artist_id>/',views.albulm_list,name='albulm_list'), ## The artist id here is defined in index.html as musician.id

    path('edit_artist/<int:artist_id>/',views.edit_artist,name='edit_artist'),

    path('edit_albulm/<int:albulm_id>/',views.edit_albulm,name='edit_albulm'),
    
    path('delete_albulm/<int:albulm_id>/',views.delete_albulm,name='delete_albulm'),

    path('delete_artist/<int:artist_id>/',views.delete_musician,name='delete_artist'),


] 