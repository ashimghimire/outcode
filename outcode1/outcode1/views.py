from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .filters import RoomFilter
from .models import Booking,Hotel,Room,Reviews
from .serializer import HotelSerializer, BookingSerializer, RoomSerializer,ReviewSerializer

@api_view(['GET'])
def get_hotels(request):
    hotels = Hotel.objects.all()
    serializedData = HotelSerializer(hotels, many=True).data
    return Response(serializedData)

@api_view(['GET'])
def get_bookings(request):
    bookings = Booking.objects.all()
    serializedData = BookingSerializer(bookings, many=True).data
    return Response(serializedData)

@api_view(['GET'])
def get_rooms(request):
    rooms = Room.objects.all()
    serializedData = RoomSerializer(rooms, many=True).data
    return Response(serializedData)

@api_view(['POST'])
def create_hotel(request):
    data = request.data
    serializer = HotelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_bookings(request):
    data = request.data
    serializer = BookingSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def cancel_bookings(request,pk):
    try:
        bookings = Booking.objects.get(pk=pk)
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=BookingSerializer(data=bookings)
    if serializer.is_valid():
        serializer.save(status=3)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_rooms(request):
    data = request.data
    serializer = RoomSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def hotel_detail(request, pk):
    try:
        hotel = Hotel.objects.get(pk=pk)
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        data = request.data
        serializer = HotelSerializer(hotel, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def booking_detail(request, pk):
    try:
        bookings = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        bookings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        data = request.data
        serializer = BookingSerializer(bookings, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def room_detail(request, pk):
    try:
        room = Room.objects.get(pk=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        data = request.data
        serializer = RoomSerializer(room, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def query_room(request, pk):
    try:
        rooms=Room.objects.get(pk=pk)
        room_filter = RoomFilter(request.query_params, queryset=rooms)
        rooms_filtered = room_filter.qs
        serializer = RoomSerializer(rooms_filtered, many=True)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data, status=status.HTTP_302_FOUND)

@api_view(['GET'])
def get_reviews(request, pk):
    reviews= Reviews.objects.filter(room_id=pk)
    serializedData = ReviewSerializer(reviews, many=True).data
    return Response(serializedData)


@api_view(['PUT', 'DELETE'])
def reviews_detail(request, pk):
    try:
        reviews = Reviews.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        data = request.data
        serializer = BookingSerializer(reviews, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_reviews(request):
    data = request.data
    serializer = ReviewSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def calculate_average_hotel_rating(request, pk):
    try:
        reviews = Reviews.objects.filter(hotel_id=pk)  # or hotel_id if you want to query for hotels

        if not reviews.exists():
            return Response({"message": "No reviews found for this room"}, status=status.HTTP_404_NOT_FOUND)

        average_rating = reviews.aggregate(Avg('rating'))['rating__avg']

        if average_rating is None:
            average_rating = 0

        return Response({"average_rating": average_rating}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
