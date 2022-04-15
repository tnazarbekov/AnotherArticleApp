from django.shortcuts import render,redirect

from .models import Articles

from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


class OurTemplateView(DetailView):
    model = Articles
    template_name = 'article_part/detail.html'
    context_object_name = 'article'


class OurUpdate(UpdateView):
    model = Articles
    template_name = 'article_part/article_create.html'
    form_class = ArticlesForm


class OurDelete(DeleteView):
    model = Articles
    template_name = 'article_part/delete.html'
    success_url = '/articles/'


# Create your views here.
def articles_home(request):
    get_all = Articles.objects.all()
    context = {
        'article': get_all
    }
    return render(request, 'article_part/article_home.html', context=context)


def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        form.save()
        return redirect('/articles')


    form = ArticlesForm()

    data = {
        'form':form,
    }

    return render(request,'article_part/article_create.html',data)
