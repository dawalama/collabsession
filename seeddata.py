from learntogether.models import *

user = User(id=1, first_name='Dawa', last_name='Sherpa', nick_name='dminer', total_points=0)
user.save()
user = User(id=2, first_name='Micheal', last_name='Kolodny', nick_name='mkolodny', total_points=0)
user.save()
user = User(id=3, first_name='Mohit', last_name='Agrawal', nick_name='mohit9', total_points=0)
user.save()
