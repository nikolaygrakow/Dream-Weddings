from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
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

        reviews = self.object.reviews.select_related('author').order_by('-created_at')

        context['reviews'] = reviews
        context['review_count'] = reviews.count()
        context['average_rating'] = reviews.aggregate(
            Avg('rating')
        )['rating__avg']

        return context

class WeddingCreateView(PermissionRequiredMixin, CreateView):
    model = Wedding
    form_class = WeddingCreateForm
    template_name = 'weddings/wedding-create.html'
    success_url = reverse_lazy('weddings:list')
    permission_required = 'weddings.add_wedding'


class WeddingEditView(PermissionRequiredMixin, UpdateView):
    model = Wedding
    form_class = WeddingEditForm
    template_name = 'weddings/wedding-edit.html'
    permission_required = 'weddings.change_wedding'

    def get_success_url(self):
        return reverse_lazy(
            'weddings:details',
            kwargs={'pk': self.object.pk}
        )

class WeddingDeleteView(PermissionRequiredMixin, DeleteView):
    model = Wedding
    template_name = 'weddings/wedding-delete.html'
    success_url = reverse_lazy('weddings:list')
    permission_required = 'weddings.delete_wedding'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = WeddingDeleteForm(instance=self.object)
        return context

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'weddings/review-create.html'

    def dispatch(self, request, *args, **kwargs):
        self.wedding = get_object_or_404(Wedding, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.wedding = self.wedding
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'weddings:details',
            kwargs={'pk': self.object.wedding.pk}
        )

class ReviewEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'weddings/review-edit.html'

    def test_func(self):
        return (
                self.request.user == self.get_object().author
                or self.request.user.is_superuser
        )

    def get_success_url(self):
        return reverse_lazy(
            'weddings:details',
            kwargs={'pk': self.object.wedding.pk}
        )

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'weddings/review-delete.html'

    def test_func(self):
        return (
                self.request.user == self.get_object().author
                or self.request.user.is_superuser
        )

    def get_success_url(self):
        return reverse_lazy(
            'weddings:details',
            kwargs={'pk': self.object.wedding.pk}
        )