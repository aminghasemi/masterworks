from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Note, User
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...
        return token

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user=request.user
    notes=Note.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)