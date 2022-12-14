from rest_framework import serializers
from api.models import Product, Image, Format, Image_Format


    
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = 'id', 'product'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['path'] = ''.join(str(instance).split('.')[0:-1])
        data['formats'] = [Format.objects.get(id=i.format_id).name for i in Image_Format.objects.filter(image_id=instance.id)]
        return data



class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

        