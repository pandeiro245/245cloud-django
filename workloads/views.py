from django.http import HttpResponse
from django.template import loader

from .models import Workload

def index(request):
    latest_workload_list = Workload.objects.order_by('-created_at')[:5]
    template = loader.get_template('workloads/index.html')
    context = {
        'latest_workload_list': latest_workload_list,
    }
    return HttpResponse(template.render(context, request))
