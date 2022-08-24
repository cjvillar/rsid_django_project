from ast import Return
from curses.ascii import CR, RS
from http.client import HTTPResponse
from urllib.request import Request

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.http.response import HttpResponseRedirect, FileResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView, FormView
from rest_framework import permissions
from rest_framework.generics import ListAPIView

from .forms import RsidsForm ,UploadFileForm
from .models import Rsids, User
from .serializers import RsidsSerializer
from rsid_search.scripts import litvar_api
from subprocess import run, PIPE
import sys

class RsidDeleteView(DeleteView):
    model = Rsids
    success_url = "/variants/rsid"
    template_name = "rsid_catalog/rsids_delete.html"


class RsidUpdateView(UpdateView):
    model = Rsids
    success_url = "/variants/rsid"
    form_class = RsidsForm


class RsidCreateView(LoginRequiredMixin, CreateView):
    model = Rsids
    success_url = "/variants/rsid"
    form_class = RsidsForm
    login_url = "/admin"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class RsidListView(LoginRequiredMixin, ListView):
    model = Rsids
    context_object_name = "rsids"
    template_name = "rsid_catalog/rsids_list.html"
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
            raise Http404("ID Doesn't Exist")  # TODO create new template for  404

        return render(request, "rsids_detail.html", {"rsid": rsid})


class RsidApiList(ListAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Rsids.objects.all()
    serializer_class = RsidsSerializer
    permission_classes = [permissions.IsAuthenticated]



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        if form.is_valid():
            out = run([sys.executable, "rsid_search/scripts/litvar_api.py", file, User],shell=False,stdout=PIPE)
            
    
            return HttpResponse("THIS FILE: " + str(request.FILES['file']))
    else:
        print(form._errors)
        form = UploadFileForm()
    return render(request, 'list', {'form': form})