# docker-entrypoint.sh

Source: junk_drawer/github/DeltaDash/backend/docker-entrypoint.sh.txt

Category: [[github-code]]

## Summary
#!/bin/bash set -e # Run Alembic migrations echo "Running database migrations..." alembic upgrade head # Start the application echo "Starting application..." exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}

## Full Content
#!/bin/bash
set -e

# Run Alembic migrations
echo "Running database migrations..."
alembic upgrade head

# Start the application
echo "Starting application..."
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}


## Metadata
- Source file: junk_drawer/github/DeltaDash/backend/docker-entrypoint.sh.txt
- Extracted: 2026-05-18
- Category: github-code
