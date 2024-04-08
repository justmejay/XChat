from django.shortcuts import render, redirect
from .models import Messages
from .forms import SentMessage

# Create your views here.

def Main(request):
     # x = Messages.objects.all()
     x = Messages.objects.all().order_by('-id')[:10]
     xcheck = x.exists()

     form  = SentMessage()

     if request.method == "POST":
          form = SentMessage(request.POST)
          print(request.POST)
          
          if 'send' in request.POST:

               if form.is_valid():
                    form.save()
                    return redirect('main')
          elif 'delete' in request.POST:
               nck = request.POST.get('nickname')

               query = Messages.objects.filter(nickname=nck)
               query.delete()
               return redirect('main')

     return render(request,'main/index.html',{"x": x, 'form': form, 'check': xcheck})
