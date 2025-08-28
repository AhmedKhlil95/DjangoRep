from django.shortcuts import render ,redirect
from django.views.generic import ListView ,DetailView , TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import ContactForm
from blog.models import Post , ContactMessage
from django.urls import reverse_lazy 
from django import forms




def index(request):
    return render(request,index.html)
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = '__all__'
class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['title','body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')

class AboutView(TemplateView):
    template_name = "about.html"


# class ContactCreateView(CreateView):
#     model = Contact
#     template_name = "contact.html"
#     fields = '__all__'

class ContactListView(ListView):
    model = ContactMessage
    template_name = "contact_list.html"
    context_object_name = 'contacts'




def contact_list(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit= True)  # Save the form data to the database
            return redirect('contact_success')
    else: 
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
