from django.db import models
from django.contrib.auth.models import User
#from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=20)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics');


    def __str__(self):
        return f'{self.user.username} Profile'

    '''
        This save() method overrides the save() method that belongs to 
        Profile's parent class, Model.
        We override save() so that we can edit the size of 'image' before
        it is saved to the database.

        To work with images, we import 'from PIL import Image' from the Pillow library.
    '''
    def save(self):

        super().save() # Running the parent class save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
