# init_db.py

Source: junk_drawer/github/DeltaDash/backend/init_db.py.txt

Category: [[github-code]]

## Summary
""" Simple database initialization script for SQLite development. Creates tables and default users. """ import sys import os sys.path.append(os.path.dirname(os.path.abspath(__file__))) from sqlalchemy import create_engine, text

## Full Content
"""
Simple database initialization script for SQLite development.
Creates tables and default users.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import create_engine, text
from app.core.config import settings
from app.core.security import get_password_hash

def init_database():
    """Initialize SQLite database with tables and default users"""
    
    # Create engine
    engine = create_engine(settings.DATABASE_URL)
    
    # Create basic tables
    with engine.connect() as conn:
        # Users table
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                full_name TEXT NOT NULL,
                hashed_password TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'viewer',
                is_active BOOLEAN NOT NULL DEFAULT TRUE,
                is_admin BOOLEAN NOT NULL DEFAULT FALSE,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """))
        
        # Insert default admin user
        admin_password_hash = get_password_hash("admin123")
        conn.execute(text("""
            INSERT OR REPLACE INTO users (id, username, full_name, hashed_password, role, is_active, is_admin)
            VALUES ('admin-id', 'admin', 'Administrator', :password, 'admin', TRUE, TRUE)
        """), {"password": admin_password_hash})
        
        # Insert default test user
        test_password_hash = get_password_hash("test123")
        conn.execute(text("""
            INSERT OR REPLACE INTO users (id, username, full_name, hashed_password, role, is_active, is_admin)
            VALUES ('test-id', 'test', 'Test User', :password, 'viewer', TRUE, FALSE)
        """), {"password": test_password_hash})
        
        conn.commit()
        print("Database initialized successfully!")
        print("Default users created:")
        print("   - Username: admin, Password: admin123 (Admin)")
        print("   - Username: test, Password: test123 (Viewer)")

if __name__ == "__main__":
    init_database()


## Metadata
- Source file: junk_drawer/github/DeltaDash/backend/init_db.py.txt
- Extracted: 2026-05-18
- Category: github-code
