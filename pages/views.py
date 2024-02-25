from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def test_view(request):
    return render(request, 'pages/test.html')

def contact_view(request):
    form = ContactForm()    #Creating the from instance
    return render(request, 'pages/contact.html', {'form': form})