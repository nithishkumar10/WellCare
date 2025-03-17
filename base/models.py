from django.db import models

class User_Model(models.Model): # Adding an explicit primary key
    username = models.CharField(unique=True, max_length=20)  # Keeping username unique
    email = models.EmailField(max_length=100, unique=True)  # Ensuring unique emails
    password = models.CharField(max_length=128)  # Increased max_length for hashing

    def __str__(self):
        return self.username + " " + self.password


class PredictionResult(models.Model):
    user = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    prediction_result = models.TextField()  # Renamed `pre` for clarity
    description = models.TextField()  # Renamed `desc`
    diet = models.TextField()  # Renamed `die` (typo)
    workout = models.TextField()  # Renamed `wrkout`
    medication = models.TextField()  # Renamed `med`
    created_at = models.DateField(auto_now_add=True)  # Consistent naming

    def __str__(self):
        return f"Prediction for {self.user.username}"


class Contact_Us(models.Model):  # Make sure class name is `ContactUs` (No underscore)
    name = models.CharField(help_text="Full Name", max_length=50)
    email = models.EmailField(help_text="Email")
    phone = models.CharField(max_length=15, help_text="Phone Number")  # Changed to CharField
    subject = models.CharField(help_text="Subject", max_length=250)
    message = models.TextField(help_text="Message")  # Changed to TextField for longer messages

    def __str__(self):
        return f"Message from {self.name}"

