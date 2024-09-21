from rest_framework.response import Response
from rest_framework.views import APIView

from forms.models import Form
from .serializers import FormSerializer


class FormList(APIView):
    def get(self, request):
        forms = Form.objects.all()
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)
