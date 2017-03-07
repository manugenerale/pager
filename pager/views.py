from django.views.generic.detail import DetailView
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Page, Block

class PageDetailView(DetailView):
    model = Page
    template_name = 'pager/page_detaiml.html'

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        return context
