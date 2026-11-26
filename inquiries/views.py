from urllib.parse import uses_params

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView

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

class WeddingInquiryDetailView(LoginRequiredMixin, DetailView):
    model = WeddingInquiry
    template_name = 'inquiries/inquiry-details.html'
    context_object_name = 'inquiry'

    def get_queryset(self):
        return WeddingInquiry.objects.filter(
            user=self.request.user
        ).select_related('wedding')

class WeddingInquiryManagementListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = WeddingInquiry
    template_name = 'inquiries/inquiry-management.html'
    context_object_name = 'inquiries'
    permission_required = 'inquiries.view_weddinginquiry'

    def get_queryset(self):
        return WeddingInquiry.objects.all().select_related('user', 'wedding').order_by('-created_at')

class WeddingInquiryManagementDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = WeddingInquiry
    template_name = 'inquiries/inquiry-management-details.html'
    context_object_name = 'inquiry'
    permission_required = 'inquiries.view_weddinginquiry'

    def get_queryset(self):
        return WeddingInquiry.objects.all().select_related('user', 'wedding')

class WeddingInquiryStatusUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'inquiries.change_weddinginquiry'

    def post(self, request, *args, **kwargs):
        inquiry = get_object_or_404(WeddingInquiry, pk=kwargs['pk'])
        status = request.POST.get('status')
        if status in (
                WeddingInquiry.StatusChoices.APPROVED,
                WeddingInquiry.StatusChoices.REJECTED,
        ) and inquiry.status == WeddingInquiry.StatusChoices.PENDING:
            inquiry.status = status
            inquiry.save(update_fields=['status'])
            messages.success(request, 'Inquiry status updated successfully!')
        else:
            messages.error(request, 'Invalid status update.')
        return redirect('inquiries:management-details', pk=inquiry.pk)