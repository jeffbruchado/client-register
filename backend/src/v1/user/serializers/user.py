from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from src.v1.user.models.user import User


class UserSerializerCreate(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    cpf = serializers.CharField(
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    phone_number = serializers.CharField(
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=6, write_only=True)

    def create(self, validated_data):
        user = User(name=validated_data['name'],
                    email=validated_data['email'],
                    address=validated_data['address'],
                    cpf=validated_data['cpf'],
                    phone_number=validated_data['phone_number']
                    )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password', 'address', 'cpf', 'phone_number')
