from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.permissions import IsAuthenticated 
# third party imports
from rest_framework.response import Response 
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer

# Create your views here.
class TestView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        # post = qs.first()
        # serializer = PostSerializer(post)
        # # it is used to serialize many row
        serializer = PostSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)









# def test_view(request):
#     data = {
#         'name': 'Sameer',
#         'address': 'Bhaktapur'
#     }

#     return JsonResponse(data)
    # if we pass data in list then
    # return JsonResponse(data,safe=False)