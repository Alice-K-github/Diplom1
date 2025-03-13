from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from diary.forms import RecordForm
from diary.models import Record
import re


def home(request):
    return render(request, 'home.html')


class RecordCreateView(LoginRequiredMixin, CreateView):
    # product_create
    model = Record
    form_class = RecordForm
    template_name = 'diary/record_form.html'
    success_url = reverse_lazy('diary:record_list')

    def form_valid(self, form):
        # Автоматическое добавление даты создания продукта, владельца
        form.instance.created_at = datetime.now()
        form.instance.owner = self.request.user
        return super().form_valid(form)


class RecordListView(LoginRequiredMixin, ListView):
    model = Record
    template_name = 'diary/record_list.html'

    def get_queryset(self):
        if not self.request.user:
            return Record.objects.none()
        return Record.objects.filter(owner=self.request.user)


class RecordDetailView(LoginRequiredMixin, DetailView):
    model = Record
    template_name = 'diary/record_detail.html'

    def get_form_class(self):
        user = self.request.user
        if not user == self.object.owner:
            raise PermissionDenied


class RecordUpdateView(LoginRequiredMixin, UpdateView):
    model = Record
    form_class = RecordForm
    template_name = 'diary/record_update_form.html'
    success_url = reverse_lazy('diary:record_form')

    def get_success_url(self):
        # После редактирования возвращает на страницу (деталей), а не на record_list
        return reverse('diary:record_detail', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        form.instance.updated_at = datetime.now()
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return RecordForm
        raise PermissionDenied


class RecordDeleteView(LoginRequiredMixin, DeleteView):
    model = Record
    template_name = 'diary/record_delete.html'
    success_url = reverse_lazy('diary:record_list')


def search(request):
    query = request.GET.get('query')
    all_records = Record.objects.all()
    records = []
    for record in all_records:
        if re.search(query, record.title) or re.search(query, record.content):
            records.append(Record.objects.get(pk=record.pk))
        else:
            pass
    context = {
        'query': query,
        'records': records
    }
    return render(request, 'diary/search.html', context)
