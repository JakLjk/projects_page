from django.urls import path
from projects import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("<int:pk>/documentation", views.project_documentation, name="project_doc"),
    path("<int:pk>/dashboard", views.project_powerbi_live, name="project_pbi")
]