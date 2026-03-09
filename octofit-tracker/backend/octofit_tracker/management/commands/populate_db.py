from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True)
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel', is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='DC', is_superhero=True)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='DC', is_superhero=True)

        # Add users to teams
        marvel.members.add(ironman)
        marvel.members.add(captain)
        dc.members.add(batman)
        dc.members.add(superman)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, date='2026-03-09')
        Activity.objects.create(user=batman, type='Cycling', duration=45, date='2026-03-09')

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='Marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='DC')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=150)
        Leaderboard.objects.create(team='DC', points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
