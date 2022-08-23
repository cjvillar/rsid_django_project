from curses.ascii import CR, RS

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView, FormView
from rest_framework import permissions
from rest_framework.generics import ListAPIView

from .forms import RsidsForm, UploadFileForm
from .models import Rsids
from .serializers import RsidsSerializer


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

class VariantFile(FormView):
    form_class = UploadFileForm
    template_name = '^VariantFile/$'  # Replace with your template.
    success_url = 'rsid_catalog/templates/rsid_catalog/rsids_list.html'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            form = "success"
            # for f in files:
            #     ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)