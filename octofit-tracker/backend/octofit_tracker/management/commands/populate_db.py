from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        get_user_model().objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            get_user_model().objects.create_user(email='ironman@marvel.com', username='ironman', team=marvel),
            get_user_model().objects.create_user(email='captain@marvel.com', username='captain', team=marvel),
            get_user_model().objects.create_user(email='batman@dc.com', username='batman', team=dc),
            get_user_model().objects.create_user(email='superman@dc.com', username='superman', team=dc),
        ]

        # Create activities
        for user in users:
            Activity.objects.create(user=user, type='run', duration=30)
            Activity.objects.create(user=user, type='cycle', duration=45)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes')
        Workout.objects.create(name='Power Yoga', description='Strength and flexibility')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
