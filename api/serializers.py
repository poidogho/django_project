from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class CourseSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=255, required=False)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    category = serializers.CharField(max_length=255)
    goals = serializers.ListField(child=serializers.CharField(max_length=255), allow_empty=True)
    rating = serializers.DecimalField(max_digits=5, decimal_places=2, required=False, allow_null=True, default=5)
    publish = serializers.BooleanField(default=False)
    free = serializers.BooleanField(default=False)
    cost = serializers.DecimalField(max_digits=10, decimal_places=2, default=0)
    dollarValue = serializers.DecimalField(max_digits=10, decimal_places=2, default=0)
    cadValue = serializers.DecimalField(max_digits=10, decimal_places=2, default=0)
    numberOfStudents = serializers.IntegerField(default=0)
    thumbnail = serializers.URLField(max_length=1024, required=False, allow_null=True)

    def validate(self, data):
        # Validate 'name' field: must not contain 'test' and is required
        name = data.get('name', '')
        if 'test' in name.lower():
            raise serializers.ValidationError({"name": "Name cannot contain 'test'"})
        if not name:
            raise serializers.ValidationError({"name": "Name is required"})

        description = data.get('description', '')
        if not description:
            raise serializers.ValidationError({"description": "Description is required"})
        
        category = data.get('category', '')
        if not category:
            raise serializers.ValidationError({"category": "Category is required"})
        
        return data