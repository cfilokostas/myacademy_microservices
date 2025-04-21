

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['is_student'] = user.is_student
        token['is_teacher'] = user.is_teacher

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Optional: include extra info in response body
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['is_student'] = self.user.is_student
        data['is_teacher'] = self.user.is_teacher

        return data
