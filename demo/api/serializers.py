from rest_framework import serializers
from .models import Student
from rest_framework.validators import ValidationError

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city'] # or fields = '__all__'
    
    # Field Level Validation
    def validate_roll(self, value):
        if value > 200:
            raise ValidationError('Only 200 seats available !!')
        return value
    
    # Object Level Validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'kartik' and city.lower() != 'saharanpur':
            raise ValidationError('city of kartik must be saharanpur')
        return data