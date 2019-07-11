from django.shortcuts import render

def index(request):
    context={
        'pesan':'Hello World'
    }
    return render(request,'index.html',context)