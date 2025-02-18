from django.db import models
from django.contrib.auth.models import User

# Attendee Model
class Attendee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    is_sponsor = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

# Calendar Event Model
class CalendarEvent(models.Model):
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('declined', 'Declined')],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.start_time} - {self.end_time})"

from django.db import models
from django.contrib.auth.models import User

# Attendee Model
class Attendee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    is_sponsor = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

# Calendar Event Model
class CalendarEvent(models.Model):
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('declined', 'Declined')],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.start_time} - {self.end_time})"

class MeetingSlot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} {self.start_time}-{self.end_time}"


class Meeting(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]

    slot = models.OneToOneField(MeetingSlot, on_delete=models.CASCADE)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_meetings')
    attendee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attended_meetings')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def confirm(self):
        self.status = 'confirmed'
        self.slot.is_booked = True
        self.slot.save()
        self.save()

    def cancel(self):
        self.status = 'canceled'
        self.slot.is_booked = False
        self.slot.save()
        self.save()

    def __str__(self):
        return f"Meeting: {self.organizer} with {self.attendee} ({self.status})"

# Done! This sets up meeting booking logic with slots and statuses. Ready for views and forms next? 😊🚀

