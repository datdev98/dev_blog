from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        kwargs['heading_img'] = 'img/home-bg.jpg'
        return kwargs

class AboutView(TemplateView):
    template_name = 'home/about.html'
    def get_context_data(self, **kwargs):
        kwargs['heading_img'] = 'img/about-bg.jpg'
        return kwargs

class ContactView(TemplateView):
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        kwargs['heading_img'] = 'img/contact-bg.jpg'
        return kwargs
