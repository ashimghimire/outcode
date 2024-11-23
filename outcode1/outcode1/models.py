from django.db import models

class Hotel(models.Model):
    name=models.CharField(max_length=200)
    locations=models.CharField(max_length=100)
    rating=models.IntegerField()
    level=models.IntegerField()

    def __str__(self):
        return self.name

class Room(models.Model):
    name=models.CharField(max_length=200)
    bed_type=models.CharField(max_length=200)
    price=models.IntegerField()
    room_type=models.CharField(max_length=200)
    size=models.IntegerField()
    level=models.IntegerField()
    hotel_id = models.ForeignKey(Hotel, to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=100)
    rating=models.IntegerField()
    hotel_id = models.ForeignKey(Hotel, to_field='id', on_delete=models.CASCADE)
    room_id=models.ForeignKey(Room, to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Booking(models.Model):
    checkin=models.DateField(auto_now=False)
    checkout=models.DateField(auto_now=100)
    status=models.IntegerField()
    adults=models.IntegerField()
    children=models.IntegerField()
    rooms=models.IntegerField()
    hotel_id = models.ForeignKey(Hotel, to_field='id', on_delete=models.CASCADE)
    room_id=models.ForeignKey(Room, to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return self.adults
