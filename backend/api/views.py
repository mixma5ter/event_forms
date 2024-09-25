from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from forms.models import Form
from .serializers import FormSerializer


class FormList(APIView):
    # Позволяет делать запросы к вашему API без проверки csrf токена
    permission_classes = [AllowAny]

    def get(self, request):
        forms = Form.objects.all()
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'__state': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'__state': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
