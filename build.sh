#!/usr/bin/env bash
# Build script for Render.com deployment

set -o errexit  # Exit on error

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt 