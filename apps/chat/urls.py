from django.urls import path

from apps.chat import views

urlpatterns = [
    path("", views.list_chats),
    path("create/", views.create_chat),
    path("<int:chat_id>/delete/", views.delete_chat),
    path("<int:chat_id>/messages/", views.show_chat_messages),
    path("<int:chat_id>/messages/send/", views.send_message),
]
