from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy

class ValidarPermisosMixin(object):
    permission_required = ''
    url_redirect = None

    def get_perms(self):
        if isinstance(self.permission_required,str):
            perms = (self.permission_required)
        else:
            perms = self.permission_required
        return perms

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('Cremeria_ToscanoApp:index')
        return self.url_redirect
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No posees el permiso para realizar esta acción')
        return redirect(self.get_url_redirect())
