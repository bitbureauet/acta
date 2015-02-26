# Create your views here.
from django.views.generic import TemplateView, DetailView, ListView, View
from page.models import CallScript
from politicians.models import Politician

class HomeView(TemplateView): 
    template_name = "page.html"
    return_to_product = False
    
    def get_context_data(self, **kwargs):
        context = {
                    "callscripts": CallScript.objects.all(), 
                    "negative": Politician.objects.filter(score = "negative"),
                    "uncertain": Politician.objects.filter(score = "uncertain"),
                    "positive": Politician.objects.filter(score = "positive")
                  }
        return context
        
