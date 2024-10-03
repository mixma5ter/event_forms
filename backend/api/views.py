from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from forms.models import Form
from .serializers import FormSerializer


FORMS_PER_PAGE = 12
MAX_PAGE_SIZE = 100


class StandardResultsSetPagination(PageNumberPagination):
    page_size = FORMS_PER_PAGE
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = MAX_PAGE_SIZE

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_pages': self.page.paginator.num_pages,  # добавляем для общего количества страниц
            'count': self.page.paginator.count,  # общее количество элементов
            'results': data
        })


class FormAPIView(APIView):
    """Класс обработки API запросов GET, POST, PUT, DELETE."""

    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination

    def get_object(self, id):
        """Получение формы по ID или возврат 404."""
        form = get_object_or_404(Form, pk=id)
        return form

    def get(self, request, id=None):
        """Получение формы по ID или списка всех форм."""
        if id is not None:
            # Запрос на получение одной формы по ID
            form = self.get_object(id)
            serializer = FormSerializer(form)
            return Response(serializer.data)
        else:
            # Запрос на получение списка форм
            forms = Form.objects.all().order_by('-updated_at')
            paginator = self.pagination_class()
            page = paginator.paginate_queryset(forms, request)

            if page is not None:
                serializer = FormSerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)
            else:
                serializer = FormSerializer(forms, many=True)
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
