from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from inquiries.forms import WeddingInquiryForm
from inquiries.models import WeddingInquiry
from weddings.models import Wedding


class WeddingInquiryCreateView(LoginRequiredMixin, CreateView):
    model = WeddingInquiry
    form_class = WeddingInquiryForm
    template_name = 'inquiries/inquiry-create.html'


    def dispatch(self, request, *args, **kwargs):
        self.wedding = get_object_or_404(Wedding, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.wedding = self.wedding
        response = super().form_valid(form)
        messages.success(self.request, 'Your inquiry has been submitted successfully!')
        return response

    def get_success_url(self):
        return reverse_lazy(
            'weddings:details',
            kwargs={'pk': self.wedding.pk}
        )

class WeddingInquiryListView(LoginRequiredMixin, ListView):
    model = WeddingInquiry
    template_name = 'inquiries/inquiry-list.html'
    context_object_name = 'inquiries'

    def get_queryset(self):
        return WeddingInquiry.objects.filter(
            user=self.request.user
        ).select_related('wedding').order_by('-created_at')