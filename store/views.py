from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from store.models import Game
from store.permissions import IsOwnerOrReadOnly
from store.serializers import GameSerializer, UserSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.

    The `highlight` field presents a hyperlink to the hightlighted HTML
    representation of the code snippet.

    The **owner** of the code snippet may update or delete instances
    of the code snippet.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
    def highlight(self, request, *args, **kwargs):
        game = self.get_object()
        return Response(game.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.

    As you can see, the collection of game instances owned by a user are
    serialized using a hyperlinked representation.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

