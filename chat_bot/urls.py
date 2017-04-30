from django.conf.urls import url,include
from .views import ChatbotView
urlpatterns = [
        
    url(r'^chat/$', ChatbotView.as_view())        
        
]
