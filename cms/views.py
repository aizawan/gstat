from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from cms.models import Resource
from cms.forms import ResourceForm


def resource_list(request, disp_mode='all'):
    if disp_mode == 'all':
        resources = Resource.objects.all().order_by('hostname')
    elif disp_mode == 'only_available':
        resources = Resource.objects.filter(is_available=True).order_by('hostname')
    elif disp_mode == 'only_unavailable':
        resources = Resource.objects.filter(is_available=False).order_by('hostname')
    else:
        raise NotImplementedError
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
