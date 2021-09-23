from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request, *args, **kwargs):
        return super(NoteList, self).list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(NoteList, self).create(request, *args, **kwargs)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


    def get(self, request, *args, **kwargs):
        # return super(NoteList, self).retrieve(request, *args, **kwargs)
        return super(NoteList, self).get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # return super(NoteList, self).update(request, *args, **kwargs)
        return super(NoteList, self).put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        # return super(NoteList, self).partial_update(request, *args, **kwargs)
        return super(NoteList, self).patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # return super(NoteList, self).destroy(request, *args, **kwargs)
        return super(NoteList, self).delete(request, *args, **kwargs)
