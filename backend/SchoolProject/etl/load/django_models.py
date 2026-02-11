from apps.CeleryApp.models import Utilisateur

def save_customers(Utilisateur):
    for c in Utilisateur:
        Utilisateur.objects.update_or_create(
            email=c["email"],
            defaults={"name": c["name"], "age": c["age"]}
        )
