#!/bin/bash
set -e

echo "Running flake8 for Python linting..."
flake8 . --exclude=.venv
if [ $? -ne 0 ]; then
    echo "Linting failed. Please fix the issues above."
    exit 1
else
    echo "Linting passed."
fi

echo "Running pytest..."
pytest tests.py -v
if [ $? -ne 0 ]; then
    echo "Tests failed. Please fix the issues above."
    exit 1
else
    echo "All tests passed."
fi