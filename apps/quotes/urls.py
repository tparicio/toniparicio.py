from django.urls import path
from django.conf.urls import url
from apps.quotes import views


urlpatterns = [
    path('authors/', views.AuthorList.as_view(), name="api-author-list"),
    url(r'^authors/(?P<pk>\d+)$', views.AuthorDetail.as_view(), name="api-author-detail"),
    path('books/', views.BookList.as_view(), name="api-book-list"),
    url(r'^books/(?P<pk>\d+)$', views.BookDetail.as_view(), name="api-book-detail"),
    path('quotes/', views.QuoteList.as_view(), name="api-quotes-list"),
    url(r'^quotes/(?P<pk>\d+)$', views.QuoteDetail.as_view(), name="api-quotes-detail"),
]