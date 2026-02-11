from apps.CeleryApp.models import Utilisateur

def get_Utilisateur():
    return list(
        Utilisateur.objects.values("id", "name", "email", "age")
    )

# njib all users from postgres