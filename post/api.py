import time

from rest_framework import viewsets

from .serializers import PostSerializer
from .models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        time.sleep(2.0)

        return qs