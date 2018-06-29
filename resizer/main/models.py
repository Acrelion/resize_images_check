from django.db import models
from . import image_specs
# Create your models here.

def generate_image_folder(instance, filename):
    import datetime
    current_time = datetime.datetime.now().strftime("%y%m%d%H%M")
    return "media/images/{0}/".format(current_time)

def save_resized_image(original, image):
    storage = original.storage
    storage(image.name, image)

class ResizedImage(models.Model):
    original = models.ImageField(upload_to='media/images')

    def save(self, *args, **kwargs):
        """
        Extension for the save method for handling
        resize of uploaded images.
        """
        #check if ImageField exists and if the image is different
        if self.original:
            #get original image and set up the generators


            image = self.original

            resize = image_specs.ResizeImg(source=image).generate()

            # medium_generator = Medium(source=original_image)
            # small_generator = Small(source=original_image)

            # medium_image = medium_generator.generate()
            # small_image = small_generator.generate()

            save_resized_image(image, resize)
            # save_resized_image(original_image, small_image, "_small")

        super(ResizedImage, self).save(*args, **kwargs)
