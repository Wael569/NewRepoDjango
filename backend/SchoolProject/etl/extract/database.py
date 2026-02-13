from apps.CeleryApp.models import Utilisateur

def get_Utilisateur():
    return list(
        Utilisateur.objects.values("id", "name", "email", "age")
    )

# extract bch ykoun min fichier JSON (JSON source ) ...


