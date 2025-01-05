from shared.supabase import create_supabase_client

supabase = create_supabase_client()

def create_restaurant(id: int, name: str, address: str, contact_number: str):
    data = {
        'id': id,
        'name': name,
        'address': address,
        'contact_number': contact_number,
    }
    
    response = supabase.table('restaurants').insert(data).execute()

    return response.data  
