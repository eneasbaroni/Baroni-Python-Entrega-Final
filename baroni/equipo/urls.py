from django.urls import path
from .views import list_members, member_detail, create_member, edit_member, delete_member

urlpatterns = [
  path('list-equipo/', list_members.as_view()),
  path('member-detail/<int:pk>', member_detail.as_view()),
  path('create-member/', create_member.as_view()),
  path('edit-member/<int:pk>', edit_member.as_view()),
  path('delete-member/<int:pk>', delete_member.as_view()),
]