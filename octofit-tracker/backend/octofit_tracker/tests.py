from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        self.user1 = User.objects.create_user(email='ironman@marvel.com', username='ironman', team=marvel)
        self.user2 = User.objects.create_user(email='batman@dc.com', username='batman', team=dc)
        Activity.objects.create(user=self.user1, type='run', duration=30)
        Workout.objects.create(name='Hero HIIT', description='High intensity')
        Leaderboard.objects.create(team=marvel, points=100)

    def test_user_team(self):
        self.assertEqual(self.user1.team.name, 'Marvel')
        self.assertEqual(self.user2.team.name, 'DC')

    def test_activity(self):
        activity = Activity.objects.get(user=self.user1)
        self.assertEqual(activity.type, 'run')

    def test_workout(self):
        workout = Workout.objects.get(name='Hero HIIT')
        self.assertEqual(workout.description, 'High intensity')

    def test_leaderboard(self):
        leaderboard = Leaderboard.objects.get(team__name='Marvel')
        self.assertEqual(leaderboard.points, 100)
