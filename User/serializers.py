from rest_framework_mongoengine import serializers


class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model = None
        fields = "__all__"