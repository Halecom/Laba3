from http import HTTPStatus

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from apps.chat import forms, models


def get_client(request):
    if request.method == "GET":
        return render(request, "chat/index.html")


def create_chat(request):
    if request.method == "POST":
        form = forms.CreateChatForm(request.POST)

        if form.is_valid():
            chat = form.save()
            return JsonResponse({"chat": {"id": chat.id}}, status=HTTPStatus.CREATED)

        return JsonResponse({"errors": form.errors}, status=HTTPStatus.BAD_REQUEST)


def delete_chat(request, chat_id):
    if request.method == "POST":
        chat = get_object_or_404(models.Chat, id=chat_id)
        chat.delete()
        return JsonResponse({"detail": "Chat successfully deleted!"}, status=HTTPStatus.NO_CONTENT)


def list_chats(request):
    if request.method == "GET":
        chats_data = []

        for chat in models.Chat.objects.all():
            chats_data.append({"id": chat.id, "name": chat.name})

        return JsonResponse(chats_data, status=HTTPStatus.OK, safe=False)


def send_message(request, chat_id):
    if request.method == "POST":
        chat = get_object_or_404(models.Chat, id=chat_id)
        form = forms.CreateMessageForm(request.POST)

        if form.is_valid():
            form.instance.chat = chat
            message = form.save()
            return JsonResponse({"message": {"id": message.id}}, status=HTTPStatus.CREATED)

        return JsonResponse({"errors": form.errors}, status=HTTPStatus.BAD_REQUEST)


def show_chat_messages(request, chat_id):
    if request.method == "GET":
        chat = get_object_or_404(models.Chat, id=chat_id)
        messages_data = []

        for message in models.Message.objects.filter(chat=chat).all():
            messages_data.append(
                {
                    "id": message.id,
                    "nickname": message.nickname,
                    "text": message.text,
                    "time": message.time,
                }
            )

        return JsonResponse(messages_data, status=HTTPStatus.OK, safe=False)
