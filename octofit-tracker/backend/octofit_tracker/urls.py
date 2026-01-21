"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api, views
from django.http import JsonResponse
import os

router = DefaultRouter()
router.register(r'users', api.UserViewSet, basename='user')
router.register(r'teams', api.TeamViewSet, basename='team')
router.register(r'activities', api.ActivityViewSet, basename='activity')
router.register(r'workouts', api.WorkoutViewSet, basename='workout')
router.register(r'leaderboard', api.LeaderboardViewSet, basename='leaderboard')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.api_root, name='api-root'),
    path('api/root_url/', lambda request: JsonResponse({
        "api_root": f"https://{os.environ.get('CODESPACE_NAME')}-8000.app.github.dev/api/" if os.environ.get('CODESPACE_NAME') else "http://localhost:8000/api/"
    })),
]
