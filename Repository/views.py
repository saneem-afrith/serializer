from django.shortcuts import render
from Repository.models import Questions, Submission
from Repository.serializers import QuestionSerializer, SubmissionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class QuestionListCreateView(APIView):
    def get(self,request):
        qs = Questions.objects.all()   #collection of questions

        #many = True means we are serializing a collection of objects, not a single object
        serializer_instance = QuestionSerializer(qs, many=True)
        #return the serialized data as a response
        return Response(serializer_instance.data)
    
    #def post(self,request):
        form_data = request.data
        Questions.objects.create(**form_data)
        return Response(data={
            "message": "Question created successfully"
        })#

    def post(self, request):
        form_data = request.data  #form_data is a dictionary containing the data sent in the request body
        serializer_instance = QuestionSerializer(data=form_data)  #create a serializer instance with the form data
        if serializer_instance.is_valid():  #check if the data is valid
            actual_data = serializer_instance.validated_data  #get the validated data from the serializer
            Questions.objects.create(**actual_data)  #create a new Question object using the validated data
            return Response(data=serializer_instance.data)  #return the serialized data as a response
        else:
            return Response(data=serializer_instance.errors)  #return the validation errors as a response

class QuestionRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):  # pk is the primary key of the question we want to retrieve
        qs = Questions.objects.get(id=pk)  #get the question object with the given primary key
        serializer_instance = QuestionSerializer(qs)  #serialize the question object
        return Response(serializer_instance.data)  #return the serialized data as a response

    def put(self,request,pk):  # pk is the primary key of the question we want to update
        form_data = request.data  #form_data is a dictionary containing the data sent in the request body
        serializer_instance = QuestionSerializer(data=form_data)  #create a serializer instance with the form data
        if serializer_instance.is_valid():  #check if the data is valid
            actual_data = serializer_instance.validated_data  #get the validated data from the serializer
            Questions.objects.filter(id=pk).update(**actual_data)  #update the question object with the given primary key using the validated data
            return Response(data=serializer_instance.data)  #return the serialized data as a response
        else:
            return Response(data=serializer_instance.errors)  #return the validation errors as a response

    def delete(self,request,pk):  # pk is the primary key of the question we want to delete
        Questions.objects.filter(id=pk).delete()  #delete the question object with the given primary key
        return Response(data={
            "message": "Question deleted successfully"
        })

class SubmissionListCreateView(APIView):
    def get(self,request):

        qs = Submission.objects.all()   #collection of submissions

        serializer_instance = SubmissionSerializer(qs, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            Submission.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)