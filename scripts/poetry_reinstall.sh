#!/bin/bash

set -e
set -x

echo "Starting complete reinstallation process..."

# Backup current configuration
echo "Backing up configuration files..."
cp pyproject.toml pyproject.toml.backup || echo "Failed to backup pyproject.toml"
cp poetry.lock poetry.lock.backup || echo "Failed to backup poetry.lock"

# Remove the current virtual environment
echo "Removing virtual environments..."
poetry env remove --all || echo "Failed to remove virtual environments"

# Clear Poetry's cache
echo "Clearing Poetry's cache..."
poetry cache clear . --all || echo "Failed to clear Poetry's cache"

# Remove existing .venv directory
echo "Removing existing .venv directory..."
rm -rf .venv || echo "Failed to remove .venv directory"

# Recreate the virtual environment and install dependencies
echo "Recreating virtual environment and installing dependencies..."
poetry install || echo "Failed to install dependencies"

# Verify the installation
echo "Verifying installation..."
poetry show || echo "Failed to show installed packages"


echo "Reinstallation process complete!"

# filepath: scripts/poetry_reinstall.sh
