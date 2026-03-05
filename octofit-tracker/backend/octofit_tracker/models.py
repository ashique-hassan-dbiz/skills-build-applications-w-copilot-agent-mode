# Models for Octofit Tracker
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	# Extend as needed for profile fields
	bio = models.TextField(blank=True, null=True)
	avatar = models.URLField(blank=True, null=True)

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True)
	members = models.ManyToManyField('User', related_name='teams')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Activity(models.Model):
	user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
	activity_type = models.CharField(max_length=50)
	duration = models.PositiveIntegerField(help_text='Duration in minutes')
	distance = models.FloatField(help_text='Distance in km', null=True, blank=True)
	calories = models.PositiveIntegerField(null=True, blank=True)
	date = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} - {self.activity_type} on {self.date}"

class Workout(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	suggested_for = models.ManyToManyField('User', related_name='suggested_workouts', blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class LeaderboardEntry(models.Model):
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
	score = models.IntegerField(default=0)
	rank = models.PositiveIntegerField(default=0)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ('user', 'team')
