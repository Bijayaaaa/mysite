from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def log_in(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        data = {}
        data['username'] = "sagarmatha"
        data['password'] = "flutter"

        return Response(data)

        return Response('serializer.data')

    elif request.method == 'POST':
        data = request.data
        if data['username'] == "sagarmatha" and data['password'] == "flutter":
            return Response("Successfully Login!")
        else:
            return Response("Login Failed! Try again")

        return Response(data)


def hello(request):
    return HttpResponse(" Hello - world ")
