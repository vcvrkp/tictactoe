from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

def welcome(request):
    if request.user.is_authenticated:
        return redirect('player_home')
    else:
        return render(request, 'tictactoe/welcome.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return render(request,'tictactoe/welcome.html')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('/temp/upload.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)