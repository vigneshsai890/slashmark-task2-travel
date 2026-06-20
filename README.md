# Task 2 — Travel Website Automation Testing

Automated test suite for **BlazeDemo** travel website using Python + Selenium + pytest.

## What's Tested

- **Flight Search** — Route selection, dropdown options, search results
- **Flight Results** — Price display, airline info, flight selection
- **Booking** — Passenger info, payment, confirmation
- **End-to-End** — Full journey from search to booking confirmation

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run Tests

```bash
# All tests
pytest

# By category
pytest -m smoke
pytest -m regression

# Generate HTML report
pytest --html=reports/report.html --self-contained-html
```

## Tech Stack

- Python 3 + Selenium 4 + pytest
- Page Object Model design pattern
- Data-driven testing with parameterized fixtures
- WebDriver Manager for automatic browser driver management

## Intern

**M Vignesh Sai** — Slash Mark Internship (June 2026)
