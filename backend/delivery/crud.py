from shared.supabase import create_supabase_client

supabase = create_supabase_client()

def create_delivery(order_id: int, user_id: int, restaurant_id: int, status: str, order_time: str):
    data = {
        'order_id': order_id,
        'user_id': user_id,
        'restaurant_id': restaurant_id,
        'status': status,
        'order_time': order_time
    }

    # Insert data ke dalam tabel 'delivery'
    response = supabase.table('delivery').insert(data).execute()

    return response.data

def update_delivery_status(order_id: int, status: str):
    data = {
        'status': status
    }

    # Update status pada tabel 'delivery' berdasarkan order_id
    response = supabase.table('delivery').update(data).eq('order_id', order_id).execute()

    return response.data

def get_deliveries():
    # Mengambil seluruh data dari tabel 'delivery'
    response = supabase.table('delivery').select('*').execute()
    return response.data

