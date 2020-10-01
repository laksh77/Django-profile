from django.shortcuts import render

# Create your views here.
# views are functions that take in requests and return the output

def home(request):

    return render(request, 'base/home.html')
