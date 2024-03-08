from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DoctorSerializer,DoctorRegistrationSerializer
from .models import Doctor
from rest_framework import status

@api_view(['POST'])
def doctorRegister(request):
    if request.method == 'POST':
        serializer = DoctorRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getDoctor(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def doctorProfile(request, pk):
    doctor = Doctor.objects.get(id=pk)
    serializer = DoctorSerializer(doctor)
    return Response(serializer.data)
