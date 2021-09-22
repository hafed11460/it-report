from rapport.forms import  RapportForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Rapport
from account.models import Account

def home(request):
    context = {
        'rapports': Rapport.objects.all()
    }
    return render(request, 'blog/index.html', context)


class RapportListView(ListView):
    model = Rapport
    template_name = 'rapport/rapport_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'objects'
    ordering = ['-id']
    paginate_by = 6


class UserRapportListView(ListView):
    model = Rapport
    template_name = 'rapport/user_rapport.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'objects'
    paginate_by = 6
    def get_queryset(self):
        user = get_object_or_404(Account, id=self.kwargs.get('pk'))
        return Rapport.objects.filter(author=user).order_by('-id')

class RapportDetailView(DetailView):
    model = Rapport



class RapportCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Rapport
    form_class = RapportForm
    template_name = 'rapport/rapport_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class RapportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Rapport
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        rapport = self.get_object()
        if self.request.user == rapport.author:
            return True
        return False


class RapportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Rapport
    success_url = '/'

    def test_func(self):
        Rapport = self.get_object()
        if self.request.user == Rapport.author:
            return True
        return False


# def about(request):
#     return render(request, 'blog/about.html', {'title': 'About'})


class RapportFilterView(ListView):
    model = Rapport
    template_name = 'rapport/rapport_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'objects'
    ordering = ['-id']
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('q','')
        startDate = self.request.GET.get('startdate','')
        endDate = self.request.GET.get('enddate','')

        if startDate and endDate:
            context["objects"]= Rapport.objects.filter(title__contains=q,date__range=[startDate,endDate])
        else:
            context["objects"] = Rapport.objects.filter(title__contains=q)
        context["q"] = self.request.GET.get('q','')

        return context
