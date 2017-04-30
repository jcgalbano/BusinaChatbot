from django.views import generic
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

class ChatbotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '171717':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
