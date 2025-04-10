from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . forms import CreateRoom
from . models import Room


# Create your views here.

def index_view(request):
    rooms = Room.objects.all()
    return render(request,'rooms/index_view.html',{'rooms':rooms})
def create_view(request):
    if request.method =='POST':
        form = CreateRoom(request.POST, request.FILES)
        if form.is_valid:
            new_room = form.save()
            messages.success(request,'Room Created Successfully!!')
            return redirect('rooms:index_view')
    else:
        form = CreateRoom()
    return render(request, 'rooms/create_view.html',{'form':form})
def update_view(request , pk):
    instance = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = CreateRoom(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room updated successfully!')
            return redirect('rooms:index_view')
    else:
        form = CreateRoom(instance=instance)
    return render(request, 'rooms/update_view.html', {'form': form})

def delete_view(request,pk):
    print('called')
    instance = get_object_or_404(Room,pk=pk)
    instance.delete()
    messages.success(request, 'Room deleted successfully!')
    return redirect('rooms:index_view')



