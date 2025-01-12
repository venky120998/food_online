from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile

@receiver(signal=post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        # Create the userprofile
        UserProfile.objects.create(user=instance)
        print('Profile is created')
    else: 
        try:
            # Update the userprofile
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # Create the userprofile if not exist(if it is created but deleted from table)
            UserProfile.objects.create(user=instance)
            print('Profile was not exist but i created one')
        print("Profile is updated")
# post_save.connect(post_save_create_profile_receiver, sender=User)

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    #print(instance.username)
    pass
