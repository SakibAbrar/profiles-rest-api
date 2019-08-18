#for post and update methods
#it allows us to create python object for input and vice versa
#we need it for inputs as we need to post or update requests!
#and it is best practice for an app to keep all serializers in a single file called serializers

from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our api view"""
    name = serializers.CharField (max_length=10)
