from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexsView(TemplateView):
    template_name = "indexs.html"


class SimpleView(TemplateView):
    template_name = "pagesTwo/simple.html"


class SalomView(TemplateView):
    template_name = "pagesTwo/salom.html"


class HtmlAndCssView(TemplateView):
    template_name = "pagesTwo/HtmlAndCss.html"


class BasicView(TemplateView):
    template_name = "pagesOne/basic.html"
