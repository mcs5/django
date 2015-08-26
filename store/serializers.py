from store.models import Game
from rest_framework import serializers
from django.contrib.auth.models import User


class GameSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='game-highlight', format='html')

    class Meta:
        model = Game
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')
                  
class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(queryset=Game.objects.all(), view_name='game-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'games')