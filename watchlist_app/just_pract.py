from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist_app.models import WatchList
from rest_framework import status
from .api.serializers import WatchListSerializer
class MovieListAV(APIView):
    def get(self, request):
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=MovieSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class MovieDetailAV(APIView):
    def get(self, request, pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def validate_name(self, value):
        if len(value)<2:
            raise serializer.ValidationError("Name is too short!")
        else:
            return value

    def validate(self, data):
        if data['title']==data['description']:
            raise serializer.ValidationError("something wrong!")
        else:
            return data

    def put(self, request, pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializer(movie)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)