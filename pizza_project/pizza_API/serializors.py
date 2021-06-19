from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Pizza, Size_item


class sizeSerializer(ModelSerializer):
    class Meta:
        model = Size_item
        fields = ['name']


class sizeserializor(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class PizzaSerializor(ModelSerializer):
    Toppings = sizeserializor(many=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Pizza
        fields = ['id','Type', 'size', 'Toppings']


    def create(self, validated_data):

        if not Size_item.objects.filter(name=validated_data['size']).exists():
            raise serializers.ValidationError({"detail": "size does not exists"})

        print(validated_data,"validated")
        return Pizza.objects.create(**validated_data)

    def update(self, instance, validated_data):
        add_toppings = self.context.get('add_Topping', False)
        print(validated_data)
        if (add_toppings):
            for item in validated_data.get('Toppings', []):
                instance.Toppings.append(item)
        else:
            instance.Toppings = validated_data['Toppings']

        instance.Type = validated_data.get("Type", instance.Type)
        instance.size = validated_data.get("size", instance.size)
        instance.save()
        return instance

    def validate_Type(self, value):
        if value.lower() == "regular" or value.lower() == "square":
            return value
        raise ValidationError(f'pizza type should be Regular or Square , but {value} was given')
