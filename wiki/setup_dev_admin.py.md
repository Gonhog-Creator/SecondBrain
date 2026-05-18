# setup_dev_admin.py

Source: junk_drawer/github/DeltaDash/backend/setup_dev_admin.py.txt

Category: [[github-code]]

## Summary
#!/usr/bin/env python3 """ Complete development setup script. This script will: 1. Run database migrations 2. Create a development admin user Only for development environment! """ import os

## Full Content
#!/usr/bin/env python3
"""
Complete development setup script.
This script will:
1. Run database migrations
2. Create a development admin user
Only for development environment!
"""

import os
import sys
import subprocess
import uuid
from sqlalchemy.orm import Session

# Add the parent directory to the path so we can import app modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.db.session import SessionLocal
from app.db.models.user import User
from app.core.security import get_password_hash
from sqlalchemy import text


def run_migrations():
    """Run database migrations."""
    print("Running database migrations...")
    try:
        result = subprocess.run([
            sys.executable, "-m", "alembic", "upgrade", "head"
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print("Database migrations completed successfully!")
            return True
        else:
            print(f"Migration failed: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("Migration timed out - database might not be running")
        return False
    except Exception as e:
        print(f"Error running migrations: {e}")
        return False


def create_dev_admin():
    """Create a development admin user if it doesn't exist."""
    
    # Check if we're in development environment
    env = os.getenv("ENVIRONMENT", "").lower()
    secret_key = os.getenv("SECRET_KEY", "")
    
    # Only allow in development if SECRET_KEY contains development indicators
    is_development = (
        "development" in secret_key.lower() or 
        "dev" in secret_key.lower() or
        env == "development" or
        "localhost" in secret_key.lower() or
        "local_dev" in secret_key.lower() or
        # Allow if the database URL contains localhost (development setup)
        "localhost" in os.getenv("DATABASE_URL", "").lower()
    )
    
    if not is_development:
        print("ERROR: This script can only be run in development environment!")
        print("   Current SECRET_KEY suggests production environment.")
        return False
    
    db: Session = SessionLocal()
    
    try:
        # Check if admin user already exists using direct SQL
        existing_admin = db.execute(text("SELECT * FROM users WHERE username = :username"), {"username": "admin"}).fetchone()
        
        if existing_admin:
            print("Admin user already exists:")
            print(f"   Username: {existing_admin.username}")
            print(f"   Admin: {existing_admin.is_admin}")
            return True
        
        # Create development admin user using direct SQL to match actual schema
        admin_id = str(uuid.uuid4())
        hashed_password = get_password_hash("admin")
        
        # Insert directly using SQL to match the actual database schema
        db.execute(
            text("INSERT INTO users (id, username, hashed_password, is_admin, created_at) VALUES (:id, :username, :hashed_password, :is_admin, NOW())"),
            {
                "id": admin_id,
                "username": "admin",
                "hashed_password": hashed_password,
                "is_admin": True
            }
        )
        db.commit()
        
        print("Development admin user created successfully!")
        print("   Username: admin")
        print("   Password: admin")
        print("   Role: admin")
        print()
        print("IMPORTANT:")
        print("   - This is for DEVELOPMENT ONLY")
        print("   - Never use these credentials in production")
        print("   - Login at: http://localhost:5173/login")
        
        return True
        
    except Exception as e:
        print(f"Error creating admin user: {e}")
        db.rollback()
        return False
    finally:
        db.close()


def main():
    print("=" * 60)
    print("Development Setup Script")
    print("=" * 60)
    print()
    
    # Check environment variables
    if not os.getenv("DATABASE_URL"):
        print("ERROR: DATABASE_URL environment variable not set!")
        print("Please set DATABASE_URL and SECRET_KEY before running this script.")
        return False
    
    if not os.getenv("SECRET_KEY"):
        print("ERROR: SECRET_KEY environment variable not set!")
        print("Please set SECRET_KEY before running this script.")
        return False
    
    # Step 1: Run migrations
    if not run_migrations():
        print("\nFailed to run migrations. Please check your database connection.")
        print("Make sure PostgreSQL is running and the database exists.")
        return False
    
    print()
    
    # Step 2: Create admin user
    if not create_dev_admin():
        print("\nFailed to create admin user.")
        return False
    
    print("\nDevelopment setup complete!")
    print("You can now login with:")
    print("  Username: admin")
    print("  Password: admin")
    return True


if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)


## Metadata
- Source file: junk_drawer/github/DeltaDash/backend/setup_dev_admin.py.txt
- Extracted: 2026-05-18
- Category: github-code
