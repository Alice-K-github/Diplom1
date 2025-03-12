from datetime import datetime
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from diary.forms import RecordForm
from diary.models import Record



def home(request):
    return render(request, 'home.html')

class RecordCreateView(CreateView):
    # product_create
    model = Record
    form_class = RecordForm
    template_name = 'diary/record_form.html'
    success_url = reverse_lazy('diary:record_list')

    def form_valid(self, form):
        # Автоматическое добавление даты создания продукта, владельца
        form.instance.created_at = datetime.now()
        '''form.instance.owner = self.request.user'''
        return super().form_valid(form)


class RecordListView(ListView):
    model = Record
    template_name = 'diary/record_list.html'

'''    def get_queryset(self):
        queryset = cache.get('my_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('my_queryset', queryset, 60 * 15)  # Кешируем данные на 15 минут
        return queryset'''

class RecordDetailView(DetailView):
    model = Record
    template_name = 'diary/record_detail.html'


class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    template_name = 'diary/record_update_form.html'
    success_url = reverse_lazy('diary:record_form')


    def get_success_url(self):
        # После редактирования возвращает на страницу (деталей), а не на record_list
        return reverse('diary:record_detail', args=[self.kwargs.get('pk')])


    def form_valid(self, form):
        # Автоматическое добавление даты редактирования продукта
        form.instance.updated_at = datetime.now()
        return super().form_valid(form)


class RecordDeleteView(DeleteView):
    model = Record
    template_name = 'diary/record_delete.html' # шаблон
    success_url = reverse_lazy('diary:record_list') # Перенаправляет на список продуктов после удаления продукта

from django.db.models import Q

def search(request):
    query = request.GET.get('query')
    print(query)
    records = Record.objects.filter(Q(title=query) | Q(content=query))
    print(records)
    context = {
        'query': query,
        'records': records
    }
    print(context)
    return render(request, 'diary/search.html', context)
