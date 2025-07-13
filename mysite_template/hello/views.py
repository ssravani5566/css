from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# This is your view
def demo(request):
    # Load the template manually using loader
    temp = loader.get_template('css13.html')
    
    # Render the template and return it as an HTTP response
    return HttpResponse(temp.render())
