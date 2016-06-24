from registration.backends.simple.views import RegistrationView as BaseRegistrationView

class RegistrationView(BaseRegistrationView):
    template_name = 'auth/signup_form.html'
