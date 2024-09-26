from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from forms.models import Form
from .serializers import FormSerializer


class FormAPIView(APIView):
    """Класс обработки API запросов GET, POST, PUT, DELETE."""

    # Позволяет делать запросы к вашему API без проверки csrf токена
    permission_classes = [AllowAny]

    def get_object(self, id):
        """Получение формы по ID или возврат 404."""
        form = get_object_or_404(Form, pk=id)
        return form

    def get(self, request, id=None):
        """Получение формы по ID или списка всех форм."""
        if id is None:
            forms = Form.objects.all().order_by('-updated_at')
            serializer = FormSerializer(forms, many=True)
            return Response(serializer.data)
        else:
            form = self.get_object(id)
            serializer = FormSerializer(form)
            return Response(serializer.data)

    def post(self, request):
        """Создание формы."""
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        """Редактирование формы."""
        form = self.get_object(id)
        serializer = FormSerializer(form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Удаление формы."""
        form = self.get_object(id)
        form.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
