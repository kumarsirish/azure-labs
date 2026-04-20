# Azure Labs

A simple Flask web application used for Azure DevOps and Azure App Service deployment labs.

## Project Overview

This project serves a single web page from the root route (`/`) and includes basic unit tests.
It is intended to demonstrate a minimal Python web app CI/CD workflow with Azure Pipelines.

## Tech Stack

- Python 3
- Flask
- Pytest / unittest
- Azure Pipelines

## Project Structure

```text
.
├── app.py                  # Flask application entry point
├── requirements.txt        # Python dependencies
├── tests/
│   └── test_main.py        # Unit tests for the root route
└── azure-pipelines*.yml    # CI/CD pipeline variants
```

## Prerequisites

- Python 3.12 (recommended to match pipeline configuration)
- pip

## Setup and Run Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open in browser:
   - `http://localhost:8000`

## Run Tests

```bash
pip install pytest pytest-cov
pytest
```

## Deployment and CI/CD

The repository contains Azure Pipelines YAML files (`azure-pipelines.yml` and variants) that:

1. Install dependencies
2. Run tests with coverage
3. Package the app as a ZIP artifact
4. Deploy to Azure App Service
