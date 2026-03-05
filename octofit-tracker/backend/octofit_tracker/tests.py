# Tests for Octofit Tracker
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Workout, LeaderboardEntry

class BasicApiTests(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='testpass')
		self.client.login(username='testuser', password='testpass')

	def test_api_root(self):
		url = reverse('api-root')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_user_list(self):
		url = reverse('user-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_team_list(self):
		url = reverse('team-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_activity_list(self):
		url = reverse('activity-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_workout_list(self):
		url = reverse('workout-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_leaderboard_list(self):
		url = reverse('leaderboardentry-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
