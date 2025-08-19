from django.urls import path
from blog import views
from blog.views import BlogListView ,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView
from blog.views import AboutView,ContactListView ,contact_list




urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/list/", ContactListView.as_view(), name="contact_success"),
    path("contact/", views.contact_list , name="contact"),


]

