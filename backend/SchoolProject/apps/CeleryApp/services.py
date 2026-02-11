from .models import Utilisateur

def get_all_Utilisateurs():
    return list(Utilisateur.objects.values("id", "name", "email", "age"))
