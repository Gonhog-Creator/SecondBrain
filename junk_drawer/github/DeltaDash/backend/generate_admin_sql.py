#!/usr/bin/env python3
"""
Generate SQL for creating development admin user.
This outputs SQL that you can run directly in your database.
"""

import uuid


def generate_admin_sql():
    """Generate SQL INSERT statement for admin user with 'admin' password."""
    
    # Pre-hashed password for "admin" (bcrypt)
    # This hash corresponds to the password "admin"
    hashed_password = "$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5NU7qvqV8hZ1e"
    
    user_id = str(uuid.uuid4())
    
    sql = f"""-- Development Admin User
-- Username: admin
-- Password: admin
-- Role: admin
-- This SQL is safe for development only
INSERT INTO users (id, username, full_name, hashed_password, role, is_active, is_admin, created_at, updated_at)
VALUES ('{user_id}', 'admin', 'Development Administrator', '{hashed_password}', 'admin', true, true, NOW(), NOW());"""
    
    return sql


def main():
    print("=" * 80)
    print("Development Admin User SQL Generator")
    print("=" * 80)
    print()
    
    sql = generate_admin_sql()
    print(sql)
    print()
    print("=" * 80)
    print("Instructions:")
    print("1. Connect to your PostgreSQL database")
    print("2. Copy and paste the SQL above")
    print("3. Execute it to create the admin user")
    print("4. Login with: admin / admin")
    print("=" * 80)


if __name__ == "__main__":
    main()
