from shared.supabase import create_supabase_client

# Mendapatkan klien Supabase
supabase = create_supabase_client()

def create_restaurant(id: int, name: str, address: str, contact_number: str):
    data = {
        'id': id,
        'name': name,
        'address': address,
        'contact_number': contact_number,
    }
    
    # Menambahkan data restoran ke tabel 'restaurants' di Supabase
    response = supabase.table('restaurants').insert(data).execute()

    return response.data  # Mengembalikan data yang baru saja ditambahkan
