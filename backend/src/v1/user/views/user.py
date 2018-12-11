from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.v1.user.serializers.user import UserSerializerCreate
from rest_framework.authtoken.models import Token


class UserView(APIView):
    """
    Creates the user.
    """


    def post(self, request):
        serializer = UserSerializerCreate(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
