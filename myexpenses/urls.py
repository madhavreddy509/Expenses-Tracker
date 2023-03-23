from django.urls import path
from . import views
urlpatterns = [
   
   path('logout/',views.logoutUser,name="logout"),
    path('',views.login_view,name="login"),
    path('register/',views.register,name="register"),
    path('expenses/',views.UserExpensesList,name="expenses"),
    path('addexpenses/',views.CreateExpense,name="addexpense"),
    path('updatexpenses/<str:pk>/',views.updateExpense,name="updateexpense"),
    path('deleteexpenses/<str:pk>/',views.deleteExpense,name="deleteexpense"),
]