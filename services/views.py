from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from services.forms import ServiceCreateForm, ServiceEditForm, ServiceDeleteForm
from services.models import Service


class ServiceCategoriesView(TemplateView):
    template_name = 'services/categories.html'

class ServiceByCategoryView(ListView):
    model = Service
    template_name = 'services/services-by-category.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.filter(
            category=self.kwargs['category']
        )

class ServiceDetailsView(DetailView):
    model = Service
    template_name = 'services/service-details.html'
    context_object_name = 'service'


class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceCreateForm
    template_name = 'services/service-create.html'

    def form_valid(self, form):
        form.instance.category = self.request.GET.get('category')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'services:category',
            kwargs={'category': self.object.category}
        )

class ServiceEditView(UpdateView):
    model = Service
    form_class = ServiceEditForm
    template_name = 'services/service-edit.html'

    def get_success_url(self):
        return reverse_lazy(
            'services:category',
            kwargs={'category': self.object.category}
        )

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'services/service-delete.html'
    success_url = reverse_lazy('services:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ServiceDeleteForm(instance=self.object)
        return context