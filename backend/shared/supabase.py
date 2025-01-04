from supabase import create_client, Client
import os

# URL dan Anon Key dari Supabase
SUPABASE_URL = "https://jrxpfkrhvnmfkmmjudvy.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpyeHBma3Jodm5tZmttbWp1ZHZ5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzU3NDM4MjMsImV4cCI6MjA1MTMxOTgyM30.JKYX44Ia_yqCAsbWO_WlRCD3f1wPYOXyf7i9Ua-kYig"

# Fungsi untuk membuat klien Supabase
def create_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

# Contoh penggunaan:
supabase = create_supabase_client()
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)