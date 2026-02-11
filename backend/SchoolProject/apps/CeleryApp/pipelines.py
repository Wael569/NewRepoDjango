from etl.extract.database import get_Utilisateur
from etl.transform.clean import filter_adults
from etl.load.django_models import save_customers

def run_users_pipeline():
    customers = get_Utilisateur()        # Extract
    customers = filter_adults(customers)  # Transform
    save_customers(customers)         # Load
    print("Users ETL done ✅")
