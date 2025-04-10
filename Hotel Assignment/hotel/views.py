from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . forms import createHotel
from . models import Hotel

# Create your views here.

def index_view(request):
    hotels = Hotel.objects.all() 
    return render(request, 'hotel/index_view.html',{'hotels':hotels})

def create_view(request):
    if request.method == 'POST':
        form = createHotel(request.POST, request.FILES)
        if form.is_valid():
            newhotel = form.save()
            messages.success(request, 'Data create successfully!')
            return redirect('hotel:index_view')
    else:
        form = createHotel()
    return render(request,'hotel/create_view.html',{'form':form})
def update_view(request , pk):
    instance = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        form = createHotel(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data updated successfully!')
            return redirect('hotel:index_view')
    else:
        form = createHotel(instance=instance)
    return render(request, 'hotel/update_view.html', {'form': form})

def delete_view(request,pk):
    instance = get_object_or_404(Hotel,pk=pk)
    instance.delete()
    messages.success(request, 'Data deleted successfully!')
    return redirect('hotel:index_view')
