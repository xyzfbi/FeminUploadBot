#!/usr/bin/env python3
"""
Test script to check Supabase client initialization
"""

try:
    from database.supabase_connection import get_supabase_sync_client, get_supabase_client
    from config.get_env import SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_KEY
    
    print("Environment variables:")
    print(f"SUPABASE_URL: {'✓ Set' if SUPABASE_URL else '✗ Missing'}")
    print(f"SUPABASE_ANON_KEY: {'✓ Set' if SUPABASE_ANON_KEY else '✗ Missing'}")
    print(f"SUPABASE_SERVICE_KEY: {'✓ Set' if SUPABASE_SERVICE_KEY else '✗ Missing'}")
    
    if not all([SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_KEY]):
        print("\n❌ Missing required environment variables!")
        print("Please create a .env file with the following variables:")
        print("SUPABASE_URL=your_supabase_url")
        print("SUPABASE_ANON_KEY=your_supabase_anon_key")
        print("SUPABASE_SERVICE_KEY=your_supabase_service_role_key")
        exit(1)
    
    print("\nTesting Supabase client creation...")
    
    # Test sync client
    sync_client = get_supabase_sync_client()
    print("✓ Sync client created successfully")
    
    # Test async client
    async_client = get_supabase_client()
    print("✓ Async client created successfully")
    
    print("\n✅ All tests passed! Supabase client is working correctly.")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Make sure all required packages are installed: pip install -r requirements.txt")
except Exception as e:
    print(f"❌ Error: {e}")
    print("Check your environment variables and Supabase configuration.") 