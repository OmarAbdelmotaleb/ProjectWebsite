from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render, redirect
from .models import ClickCount

from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect

@csrf_protect
@cache_page(300)
def index(request):
    if request.method == 'POST':  # If the button was clicked
        obj, created = ClickCount.objects.get_or_create(id=1)
        obj.count += 1
        obj.save()
        return redirect('index')  # Reload the page

    obj, created = ClickCount.objects.get_or_create(id=1)
    context = {'count': obj.count}
    return render(request, 'index.html', context)
