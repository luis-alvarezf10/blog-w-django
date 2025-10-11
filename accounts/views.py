from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    # formulario de creacion de usuario, funcion propia de django
    form_class = UserCreationForm
    # redirecciona a la pagina de login
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

