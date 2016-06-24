from registration.backends.simple.views import RegistrationView as BaseRegistrationView

class RegistrationView(BaseRegistrationView):
    success_url = 'auth_signup_complete'
    template_name = 'auth/signup_form.html'
