from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from weddings.forms import WeddingCreateForm, WeddingEditForm, WeddingDeleteForm, ReviewForm
from weddings.models import Wedding, Review


class WeddingListView(ListView):
    model = Wedding
    template_name = 'weddings/wedding-list.html'
    context_object_name = 'weddings'
    ordering = ['pk']

class WeddingDetailsView(DetailView):
    model = Wedding
    template_name = 'weddings/wedding-details.html'
    context_object_name = 'wedding'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        reviews = self.object.reviews.all().order_by('-created_at')

        context['reviews'] = reviews
        context['review_count'] = reviews.count()
        context['average_rating'] = reviews.aggregate(
            Avg('rating')
        )['rating__avg']

        return context

class WeddingCreateView(CreateView):
    model = Wedding
    form_class = WeddingCreateForm
    template_name = 'weddings/wedding-create.html'
    success_url = reverse_lazy('weddings:list')


class WeddingEditView(UpdateView):
    model = Wedding
    form_class = WeddingEditForm
    template_name = 'weddings/wedding-edit.html'

    def get_success_url(self):
        return reverse_lazy(
            'weddings:details',
            kwargs={'pk': self.object.pk}
        )

class WeddingDeleteView(DeleteView):
    model = Wedding
    template_name = 'weddings/wedding-delete.html'
    success_url = reverse_lazy('weddings:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = WeddingDeleteForm(instance=self.object)
        return context

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'weddings/review-create.html'

    def dispatch(self, request, *args, **kwargs):
        self.wedding = get_object_or_404(Wedding, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.wedding = self.wedding
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'weddings:details',
            kwargs={'pk': self.object.wedding.pk}
        )