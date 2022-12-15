from django.db import models
from PIL import Image as PIL_Image
from io import BytesIO
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import FileExtensionValidator


class Product(models.Model):

    class Status(models.TextChoices):
        in_stock = 'in_stock'
        on_request = 'on_request'
        expected = 'expected'
        out_of_stock = 'out_of_stock'
        not_produced = 'not_produced'

    name = models.CharField(max_length=50)
    article = models.CharField(max_length=50)
    price = models.FloatField()
    status = models.CharField(choices=Status.choices, max_length=50)
    
    def __str__(self):
        return f'{self.name} - {self.price} - {self.article}'



class Image(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images',)
    path = models.ImageField(upload_to='', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'webp'])])

    def save(self, *args, **kwargs):
        ext = str(self).split('.')[-1].lower()
        filename = ''.join(str(self).split('/')[-1].split('.')[0:-1])

        # save image with ORIGINAL format
        super(Image, self).save()

        try:
            Image_Format.objects.filter(image_id=self.id).delete()
        except:
            print("there are no image_format records yet")

        # associate image with format in db by Image_Format table
        image_ext = Format.objects.get_or_create(name=ext)
        image_ext_id = image_ext[0].id
        Image_Format.objects.get_or_create(image_id=self.id, format_id=image_ext_id)

        if ext != 'webp':
            output_thumb = BytesIO()
            with PIL_Image.open(self.path) as img:
                img.save(output_thumb, format='WEBP', quality=80)
                self.path = InMemoryUploadedFile(
                    output_thumb,
                    'ImageField',
                    f'{filename}.webp',
                    'image/webp',
                    sys.getsizeof(output_thumb),
                    None,
                )
            # save image with WEBP format
            super(Image, self).save()

            # associate image with format in db by Image_Format table
            webp = Format.objects.get_or_create(name='webp')
            webp_id = webp[0].id
            Image_Format.objects.get_or_create(image_id=self.id, format_id=webp_id)



    def __str__(self):
        return f'{self.path}'



class Format(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name}"



class Image_Format(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    format = models.ForeignKey(Format, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.image} - {self.format}'