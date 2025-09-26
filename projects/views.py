import os
from django.shortcuts import render, get_object_or_404
from django.http import Http404, FileResponse
from projects.models import Project

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects":projects
    }
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project":project
    }
    return render(request, "projects/project_detail.html", context)


def project_documentation(request, pk):
    project = get_object_or_404(Project, pk=pk)
    f = project.documentation_file
    if not f:
        raise Http404("No documentation file")
    resp = FileResponse(f.open("rb"), content_type="application/pdf")
    filename = os.path.basename(f.name)
    if request.GET.get("download") == "1":
        resp["Content-Disposition"] = f'attachment; filename="{filename}'
    else:
        resp["Content-Disposition"] = f'inline; filename="{filename}'
    return resp

def project_powerbi_live(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        "project":project
    }
    return render(request, "projects/project_pbi_live.html", context)