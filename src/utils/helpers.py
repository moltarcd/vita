import json

def safe_json_response(response):
    """Safely parse JSON response, handling empty responses"""
    if response.status_code == 204 or not response.content:
        return {}  # Return empty dict for no content responses
    
    try:
        return response.json()
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response", "text": response.text[:100]}  # Limit text length

def response_to_dict(response):
    """Convert response to dictionary with status and data"""
    return {
        "status_code": response.status_code,
        "data": safe_json_response(response),
        "headers": dict(response.headers),
        "url": response.url
    }