from supabase import create_client, Client
from supabase._sync.client import SyncClient
from config.get_env import SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_KEY

_supabase_client: Client = None
_supabase_sync_client: SyncClient = None


def get_supabase_client() -> Client:
    """Get the async Supabase client instance."""
    global _supabase_client
    if _supabase_client is None:
        _supabase_client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
    return _supabase_client


def get_supabase_sync_client() -> SyncClient:
    """Get the sync Supabase client instance."""
    global _supabase_sync_client
    if _supabase_sync_client is None:
        _supabase_sync_client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)
    return _supabase_sync_client


async def get_supabase() -> Client:
    """Async function to get Supabase client (for backward compatibility)."""
    return get_supabase_client()
