from django.urls import path
from .views import polls_list, polls_detail

urlpatterns = [
	path("polls/", polls_list, name="polls_list"),
	path("polls/<int:pk>", poll_detail, name="polls_detail")
]
