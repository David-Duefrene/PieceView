from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseBadRequest
from django.views.generic.base import View


class AuthAjaxOnlyMixin(View):
    """
    Mixing ensures they view is only working via Ajax requests with
    authenticated users. Mixin inherits from View, and overrides the dispatch
    method.
    """

    def dispatch(self, request, *args, **kwargs):
        print("Inside the Mixin")
        if not request.is_ajax():
            return HttpResponseBadRequest()

        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())

        return super().dispatch(request, *args, **kwargs)
