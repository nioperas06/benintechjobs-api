from .models import Job, Quote
from .serializers import JobSerializer, QuoteSerializer
from rest_framework import generics


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.filter(active=True)
    serializer_class = JobSerializer


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class QuoteList(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer