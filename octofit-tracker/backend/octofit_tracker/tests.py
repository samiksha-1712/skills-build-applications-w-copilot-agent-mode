from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@hero.com', name='Test Hero', team='Marvel')
        self.assertEqual(user.name, 'Test Hero')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(team.name, 'Marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email='test@hero.com', name='Test Hero', team='Marvel')
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2026-03-09')
        self.assertEqual(activity.type, 'Running')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='Marvel')
        self.assertEqual(workout.name, 'Pushups')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Marvel', points=100)
        self.assertEqual(leaderboard.team, 'Marvel')
