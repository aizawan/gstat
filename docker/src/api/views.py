import json
from collections import OrderedDict
from django.http import HttpResponse
from cms.models import Resource


def render_json_response(request, data, status=None):
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response


def get_json(request, resource_name=None):
    if resource_name is None:
        resources = []
        for resource in Resource.objects.all().order_by('hostname'):
            dict_ = OrderedDict([
                ('hostname', resource.hostname),
                ('is_available', resource.is_available),
                ('locking_user', resource.locking_user),
            ])
            resources.append(dict_)

        data = OrderedDict([('resources', resources)])
        return render_json_response(request, data)
    else:
        resource = Resource.objects.filter(hostname=resource_name)[0]
        dict_ = OrderedDict([
            ('hostname', resource.hostname),
            ('is_available', resource.is_available),
            ('locking_user', resource.locking_user),
        ])
        data = OrderedDict([('resources', [dict_])])
        return render_json_response(request, data)
