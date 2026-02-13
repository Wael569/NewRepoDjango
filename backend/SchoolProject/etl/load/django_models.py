from apps.CeleryApp.models import Utilisateur
from apps.CeleryApp.serializers import UtilisateurSerializer


def save_customers(data):
    for customer in data:
        try:
            instance = Utilisateur.objects.get(email=customer["email"])
            serializer = UtilisateurSerializer(instance, data=customer)
        except Utilisateur.DoesNotExist:
            serializer = UtilisateurSerializer(data=customer)

        if serializer.is_valid():
            serializer.save()
        else:
            print("Validation error:", serializer.errors)
