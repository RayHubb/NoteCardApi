from django.shortcuts import (
        get_object_or_404,
        HttpResponseRedirect,
        render,
    )
from django.http import Http404
from .serializers import NoteCardSerializer
from .serializers import CollectionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NoteCard
from .models import Collection

# Create your views here.

class CollectionList(APIView):
    def get(self, request):
        collection  = Collection.objects.all()
        collection_serializer = CollectionSerializer(collection, many=True)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteCardDetail(APIView):
    def get_object_or_404(self, pk):
        try:
            return Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            raise Http404

    def get(request, collection_id):
        collection_obj = get_object_or_404(Collection, id=collection_id)
        notecards = NoteCard.objects.filter(collection=collection_obj)
        serializer = NoteCardSerializer(notecards, many=true)
        return  Response(serializer.data)


    def post(self, request, collection_id):
        print(collection_id)
        print(request.data)
        new_notecard = NoteCard(question=request.data['question'], answer=request.data['answer'], collection_id=collection_id)
        new_notecard.save()
        return Response(new_notecard, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)*/

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_200_OK)


class ReplyDetail(APIView):
    def get_object(self, pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        reply = self.get_object(pk)
        serializer = ReplySerializer(reply)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        reply = self.get_object(pk)
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reply = self.get_object(pk)
        reply.delete()
        return Response(status=status.HTTP_200_OK)
