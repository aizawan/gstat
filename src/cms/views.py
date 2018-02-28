from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.functions import Substr, Concat, Length
from django.db.models import Value
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from cms.models import Resource
from cms.forms import ResourceForm


def resource_list(request, disp_mode='all'):
    if disp_mode == 'all':
        resources = Resource.objects.all()
    elif disp_mode == 'only_available':
        resources = Resource.objects.filter(is_available=True)
    elif disp_mode == 'only_unavailable':
        resources = Resource.objects.filter(is_available=False)
    else:
        raise NotImplementedError
    # Change according to your your environment.
    # Our environment: "gpu1", "gpu2" .... 
    resources = resources.order_by(Substr('hostname', 1, 3), 
                                   Length('hostname'),
                                   Substr('hostname', 3))
    return render(request,
                  'cms/resource_list.html',
                  {'resources': resources})


@csrf_exempt
def resource_edit(request, resource_name=None):
    if resource_name:
        resource = get_object_or_404(Resource, pk=resource_name)
    else:
        resource = Resource()

    if request.method == 'POST':
        form = ResourceForm(request.POST,
                            instance=resource)
        if form.is_valid():
            print(request.body)
            resource = form.save(commit=False)
            resource.save()
            return redirect('cms:resource_list')
        print('invalid')

    else:
        form = ResourceForm(instance=resource)
    return render(request,
                  'cms/resource_edit.html',
                  dict(form=form,
                       resource_name=resource_name))


@csrf_exempt
def resource_del(request, resource_name):
    resource = get_object_or_404(Resource, pk=resource_name)
    resource.delete()
    return redirect('cms:resource_list')
