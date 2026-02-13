import pandas as pd


def clean_utilisateurs(data):
    # Convert JSON (list of dict) to DataFrame
    df = pd.DataFrame(data)
    # Remove duplicates
    df = df.drop_duplicates()
    # rows maghir email
    df = df.dropna(subset=["name", "email"])
    # Clean name (strip spaces + capitalize)
    df["name"] = df["name"].str.strip().str.title()
    # Normalize email (lowercase)
    df["email"] = df["email"].str.lower().str.strip()
    # Convert age to integer
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    # Remove invalid ages (null or negative)
    df = df[df["age"].notnull()]
    df = df[df["age"] > 0]
    # Convert back to list of dictionaries
    cleaned_data = df.to_dict(orient="records")
    return cleaned_data
