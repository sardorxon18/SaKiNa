# from django.urls import path
# from .views import IndexsView, SimpleView, SalomView, HtmlAndCssView, BasicView

# urlpatterns = [
#     path("", IndexsView.as_view(), name="Indexs"),
#     path("simple/", SimpleView.as_view(), name="simle"),
#     path("salom/", SalomView.as_view(), name="salom"),
#     path("sakina/", HtmlAndCssView.as_view(), name="sakina"),
#     path("basic/", BasicView.as_view(), name="Basic"),
# ]

from django.urls import path
from pagesapp import views

urlpatterns = [
    path("", views.IndexsView.as_view(), name="indexs"),
    path("simple/", views.SimpleView.as_view(), name="simple"),
    path("salom/", views.SalomView.as_view(), name="salom"),
    path("htmlandcss/", views.HtmlAndCssView.as_view(), name="htmlandcss"),
    path("basic/", views.BasicView.as_view(), name="basic"),
]
