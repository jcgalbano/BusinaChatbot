from django.conf.urls import url,include
from .views import ChatbotView
from .views import landingpageView

urlpatterns = [
    url(r'^$', landingpageView),
    url(r'^chat/$', ChatbotView.as_view())        
        
]
