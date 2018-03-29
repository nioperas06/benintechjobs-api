from .models import Job
from .serializers import JobSerializer
from rest_framework import generics


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.filter(active=True)
    serializer_class = JobSerializer


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer