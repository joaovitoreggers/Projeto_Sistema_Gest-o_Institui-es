from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostModelSerializer


class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

class PostRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    