from .serializers import LinkSerializer
from .models import Links
from rest_framework import generics


# Create your views here.
class PostListAPI(generics.ListAPIView):
    queryset = Links.objects.filter(active= True)
    serializer_class = LinkSerializer


class PostCreateAPI(generics.CreateAPIView):
    queryset= Links.objects.filter(active = True)
    serializer_class = LinkSerializer


class PostDetailAPI(generics.RetrieveAPIView):
    queryset = Links.objects.filter(active = True)
    serializer_class = LinkSerializer


class PostUpdateAPI(generics.UpdateAPIView):
    queryset = Links.objects.filter(active = True)
    serializer_class = LinkSerializer


class PostDeleteAPI(generics.DestroyAPIView):
    queryset = Links.objects.filter(active = True)
    serializer_class = LinkSerializer

