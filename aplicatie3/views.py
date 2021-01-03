from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
# ListView => Afisare date
# CreateView => Adaugare date
# UpdateView => Modificare date
# DeleteView => Stergere date
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie3.forms import JobsForm
from aplicatie3.models import Jobs


class HomeIndex(LoginRequiredMixin, ListView):
    model = Jobs
    template_name = 'aplicatie3/jobs_index.html'
    context_object_name = 'all_jobs'


class CreateJobsView(LoginRequiredMixin, CreateView):
    model = Jobs
    # fields = ['name', 'website', 'type', 'active', 'location']
    form_class = JobsForm
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie3:home')


class UpdateJobsView(LoginRequiredMixin, UpdateView):
    model = Jobs
    # fields = ['name', 'website', 'type', 'active', 'location']
    form_class = JobsForm
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie3:modificare', kwargs={'pk': self.kwargs['pk']})