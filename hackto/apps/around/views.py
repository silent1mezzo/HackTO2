from django.shortcuts import  render_to_response
from django.template import RequestContext

# Create your views here.
def index(request):
    template_name = 'base.html'
    context = RequestContext(request)
    dict = {}

    return render_to_response(
        template_name,
        dict,
        context,
    )
