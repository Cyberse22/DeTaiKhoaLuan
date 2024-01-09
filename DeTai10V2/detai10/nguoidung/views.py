from rest_framework import viewsets, generics, status, parsers, permissions
from rest_framework.decorators import action
from rest_framework.views import Response
from nguoidung.models import NguoiDung
from nguoidung import serializers, paginators


class NguoiDungViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = NguoiDung.objects.filter()
    serializer_class = serializers.NguoiDungSerializer
    parser_classes = [parsers.MultiPartParser]

    def get_permissions(self):
        if self.action.__eq__("current_user"):
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False)
    def current_user(self, request):
        return Response(serializers.ProfileSerializer(request.user).data)
