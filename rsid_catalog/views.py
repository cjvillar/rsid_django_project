from curses.ascii import CR, RS
from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView ,ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from .forms import RsidsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import RsidsSerializer
from rest_framework.generics import ListAPIView
from rest_framework import permissions


from .models import Rsids


class RsidDeleteView(DeleteView):
    model = Rsids
    success_url = '/variants/rsid'
    template_name= 'rsid_catalog/rsids_delete.html'

class RsidUpdateView(UpdateView):
    model = Rsids
    success_url = '/variants/rsid'
    form_class = RsidsForm


class RsidCreateView(LoginRequiredMixin, CreateView):
    model = Rsids
    success_url = '/variants/rsid'
    form_class = RsidsForm
    login_url = "/admin"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class RsidListView(LoginRequiredMixin, ListView):
    model = Rsids
    context_object_name = 'rsids'
    template_name= 'rsid_catalog/rsids_list.html' 
    login_url = "/admin"

    # def get_queryset(self):
    #     return self.request.user.notes.all()
    def get_queryset(self):
        return self.request.user.rsids.all()

class RsidDetailView(DetailView):
    model = Rsids
    context_object_name = "rsid"

    def detail(request, pk):
        try:
            rsid = Rsids.objects.get(pk=pk)
        except Rsids.DoesNotExist:
            raise Http404("ID Doesn't Exist") # TODO create new template for  404
    
        return render(request, 'rsids_detail.html', {'rsid':rsid})


class RsidApiList(ListAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Rsids.objects.all()
    serializer_class = RsidsSerializer
    permission_classes = [permissions.IsAuthenticated]