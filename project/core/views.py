from django.views.generic import DetailView
from django.views.generic.edit import FormView

from .forms import *


class RegisterFormView(FormView):
    form_class = CustomUserCreationForm
    success_url = "/login/"
    template_name = "core/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class Profile(DetailView):
    model = get_user_model()
    template_name = "core/profile.html"
