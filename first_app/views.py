from django.shortcuts import render
from first_app import forms
from .models import Musician, Albulm
from django.db.models import Avg

# Create your views here.

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {
        'title':'Home Page',
        'musician_list' : musician_list
    }
    return render(request, 'first_app/index.html', context = diction)





def musician_form(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {
        'title':'Add Musician',
        'musician_form' : form,
    }
    return render(request, 'first_app/musician_form.html', context = diction)



def albulm_form(request):
    form = forms.AlbulmForm()

    if request.method == 'POST':
        form = forms.AlbulmForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {
        'title':'Add Albulm',
        'albulm_form' : form,
    }
    return render(request, 'first_app/albulm_form.html', context = diction)




def albulm_list(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    albulm_list = Albulm.objects.filter(artist=artist_id)
    artist_rating = Albulm.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))

    diction = {
        'title':'List of Albulms',
        'artist_info':artist_info,
        'albulm_list' : albulm_list,
        'artist_rating' : artist_rating
    }
    return render(request, 'first_app/albulm_list.html', context = diction)





def edit_artist(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=artist_info )
         ## This is important because without this it wont save the updated data to the pk, it would just create another object into the table

        if form.is_valid():
            form.save(commit=True)
            return albulm_list(request,artist_id)

    diction = {
        'edit_form' : form,
    }
    return render(request, 'first_app/edit_artist.html', context = diction)





def edit_albulm(request,albulm_id):
    albulm_info = Albulm.objects.get(pk=albulm_id)
    form = forms.AlbulmForm(instance=albulm_info)
    diction = {}

    if request.method == 'POST':
        form = forms.AlbulmForm(request.POST, instance=albulm_info )

        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text':'Albulm Successfully Updated'})

    diction.update({'edit_form' : form,})
    diction.update({'albulm_id':albulm_id})
    return render(request, 'first_app/edit_albulm.html', context=diction )



def delete_albulm(request,albulm_id):
    albulm = Albulm.objects.get(pk=albulm_id).delete()

    diction = {'delete_success':'Albulm Deleted Successfully'}
    return render(request,'first_app/delete.html',context = diction)



def delete_musician(request,artist_id):
    artist = Musician.objects.get(pk=artist_id).delete()

    diction = {'delete_success':'Musician Deleted Successfully'}
    return render(request,'first_app/delete.html',context = diction)
