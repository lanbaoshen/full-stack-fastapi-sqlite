#!/usr/bin/env bash

export SERVER_NAME="Lanbao"
export SERVER_HOST="http://localhost"
export PROJECT_NAME="Demo"
export SENTRY_DSN=""
export SQLALCHEMY_DATABASE_URI="sqlite:///./demo_app.db"
export FIRST_SUPERUSER=admin
export FIRST_SUPERUSER_EMAIL=admin@test.com
export FIRST_SUPERUSER_PASSWORD=admin

export PYTHONPATH=backend
cd $(dirname $0)
# Create initial data in DB
python3 backend/app/initial_data.py

uvicorn backend.app.main:app --port 8080 --reload
