from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer

class ProfileAPIView(APIView):
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Assuming you have proper authentication set up
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        profile = request.user.profile  # Assuming you have a OneToOne relationship between User and Profile
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
