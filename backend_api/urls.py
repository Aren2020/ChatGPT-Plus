from django.urls import path
from . import views

urlpatterns = [
    path('',views.SectionHomeView.as_view()),
    path('chat/',views.SectionDetailsView.as_view(),),
    path('chat/<slug:slug>',views.SectionDetailsView.as_view(),),
    path('supported-languages/',views.SupportedLanguagesView.as_view(),)
]