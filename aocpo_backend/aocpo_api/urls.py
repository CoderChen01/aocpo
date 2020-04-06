#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from .views import login_register, task_manage, analysis_page
urlpatterns = [
    path('login/', login_register.Login.as_view()),
    path('register/', login_register.SignIn.as_view()),
    path('register/check_username', login_register.SignIn.as_view()),
    path('task_manager/addition/', task_manage.TaskManage.as_view()),
    path('task_manager/removing/', task_manage.TaskManage.as_view()),
    path('task_manager/recovering/', task_manage.Recover.as_view()),
    path('task_manager/upgrade/', task_manage.TaskManage.as_view()),
    path('task_manager/tasks', task_manage.TaskManage.as_view()),
    path('task_manager/schools', task_manage.SearchSchool.as_view()),
    path('analysis_page/posts_data', analysis_page.GetData.as_view()),
    path('analysis_page/users_analysis_data', analysis_page.GetUserAnalyseData.as_view()),
    path('analysis_page/posts_analysis_data', analysis_page.GetPostsAnalysisData.as_view())
]
