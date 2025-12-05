# CS188 Building an API in Python

# Python Weather API

This is a Flask-based rest API that wraps the Open-Meteo public weather API.
It uses both GET and POST endpoints for retrieving hourly temperature 
based on latitude, longitude, and temperature units.

## External API Used:
- Open-Meteo Weather API
- Base URL: https://api.open-meteo.com/v1/forecast
- No email or code required

## API Endpoints:

### GET /weather
Gets hourly temperature data using query parameters.

**Query Parameters:**
- lat (float): Latitude
- lon (float): Longitude
- unit (string): "fahrenheit" or "celsius"

**Example:**
```
/weather?lat=41.6&lon=-93.6&unit=fahrenheit
```

### POST /weather
Gets hourly temperature data using a JSON request body.

**JSON Body:**
```json
{
  "lat": 41.6,
  "lon": -93.6,
  "unit": "celsius"
}
```

## Response Storage
All API responses are saved locally:
- GET responses → data:get_responses.jsonl
- POST responses → data:post_responses.jsonl

Each entry includes a timestamp and the full JSON response.

## Testing
Unit tests are written using pytest and validate:
- Successful GET and POST requests
- Error handling for missing parameters
- Tests are automatically run using GitHub Actions.

## Buggy Commit and Revert
For the assignment, a buggy commit was intentionally introduced and then reverted.
- Buggy commit: 4084212
- Revert commit: 39d4317
