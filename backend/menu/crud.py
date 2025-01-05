from shared.supabase import create_supabase_client

supabase = create_supabase_client()

def create_menu(id: int, restaurant_id: int, name: str, price: float, waste_saved: str):
    data = {
        'id': id,
        'restaurant_id': restaurant_id,
        'name': name,
        'price': price,
        'waste_saved': waste_saved,
    }
    
    response = supabase.table('menu').insert(data).execute()

    return response.data  