#!/usr/bin/env python3
"""
Development-only script to create an admin user.
This should only be used in development environment, never in production.
"""

import os
import sys
from sqlalchemy.orm import Session

# Add the parent directory to the path so we can import app modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.db.session import SessionLocal
from app.db.models.user import User
from app.core.security import get_password_hash


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
        "localhost" in secret_key.lower()
    )
    
    if not is_development:
        print("ERROR: This script can only be run in development environment!")
        print("   Current SECRET_KEY suggests production environment.")
        return False
    
    db: Session = SessionLocal()
    
    try:
        # Check if admin user already exists
        existing_admin = db.query(User).filter(User.username == "admin").first()
        
        if existing_admin:
            print("Admin user already exists:")
            print(f"   Username: {existing_admin.username}")
            print(f"   Role: {existing_admin.role}")
            print(f"   Admin: {existing_admin.is_admin}")
            return True
        
        # Create development admin user
        admin_user = User(
            username="admin",
            full_name="Development Administrator",
            hashed_password=get_password_hash("admin"),
            role="admin",
            is_active=True,
            is_admin=True
        )
        
        db.add(admin_user)
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


if __name__ == "__main__":
    print("=" * 60)
    print("Development Admin User Creator")
    print("=" * 60)
    print()
    
    success = create_dev_admin()
    
    if success:
        print("\nDevelopment setup complete!")
    else:
        print("\nFailed to create development admin user.")
        sys.exit(1)
