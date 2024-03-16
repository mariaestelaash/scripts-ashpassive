from django.urls import path
from .views import ImportView

urlpatterns = [
    # path("", index, name="index"),
    path("",ImportView.as_view()),
    # path("",index)
]