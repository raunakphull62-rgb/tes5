python
import os
from supabase import create_client, Client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY")
SUPABASE_SERVICE_KEY = os.environ.get("SUPABASE_SERVICE_KEY")

supabase_url: str = SUPABASE_URL
supabase_key: str = SUPABASE_ANON_KEY
supabase: Client = create_client(supabase_url, supabase_key)

def get_db():
    return supabase