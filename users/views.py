from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics , status, permissions
from rest_framework.response import Response
#from rest_framework.views import APIView
from . serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken , TokenError

# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

#Function Based Views

# Register
@api_view(['POST'])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        tokens = get_tokens_for_user(user)
        return Response({'user' : UserSerializer(user).data, 'tokens':tokens}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login 
@api_view(['POST'])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        tokens = get_tokens_for_user(user)
        return Response({'user': UserSerializer(user).data, 'tokens': tokens})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Profile
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def profile_view(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


# Logout (blacklist token)
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def logout_view(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"detail": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
    except KeyError:
        return Response({"error": "Refresh token not provided"}, status=status.HTTP_400_BAD_REQUEST)
    except TokenError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
# Class based views 

# class RegisterView(generics.CreateAPIView):
#     serializer_class = RegisterSerializer

# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data
#             tokens = get_tokens_for_user(user)
#             return Response({'user': UserSerializer(user).data, 'tokens': tokens})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class userProfileView(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = UserSerializer

#     def get_object(self):
#         return self.request.user

