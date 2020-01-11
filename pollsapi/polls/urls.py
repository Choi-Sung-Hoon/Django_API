from django.urls import path
from rest_framework.routers import DefaultRouter

# from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote
from .apiviews import PollViewSet, UserCreate, LoginView

router = DefaultRouter()
router.register('polls', PollViewSet)

urlpatterns = [
    # path("polls/", polls_list, name="polls_list"),
    # path("polls/<int:pk>", polls_detail, name="polls_detail")
    # path("polls/", PollList.as_view(), name="polls_list"),
    # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("login/", LoginView.as_view(), name="login"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
]

urlpatterns += router.urls
