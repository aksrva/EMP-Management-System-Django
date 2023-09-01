from django.urls import path
from emp_app.views import *
urlpatterns = [
    path("", index),
    path("add-emp", add_emp),
    path("delete-emp/<int:emp_id>", del_emp),
    path("update-emp/<int:emp_id>", update_emp)
]
