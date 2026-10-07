from supabase import create_client
from app.core.config import settings

supabase = create_client(
    settings.supabase_url,
    settings.supabase_publishable_key,
)

email = input("Email: ")
password = input("Password: ")

response = supabase.auth.sign_in_with_password(
    {
        "email": email,
        "password": password,
    }
)

if response.session:
    print("\nLOGIN SUCCESSFUL")
    print("\nACCESS TOKEN:\n")
    print(response.session.access_token)
else:
    print("\nLogin failed")
    print(response)
