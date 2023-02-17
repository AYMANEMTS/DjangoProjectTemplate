from django.urls import path
from .views import  ModerList,ModerDetail,Creat,Update,Delet,Mylogin


app_name = 'my_admin'


urlpatterns = [
    path("", ModerList.as_view(), name="list"),
    path("login", Mylogin.as_view(), name="login"),
    path("detail/<int:pk>/", ModerDetail.as_view(), name="detail"),
    path("creat/", Creat.as_view(), name="create"),
    path("update/<int:pk>/", Update.as_view(), name="update"),
    path("delet/<int:pk>/", Delet.as_view(), name="delet"),
]
