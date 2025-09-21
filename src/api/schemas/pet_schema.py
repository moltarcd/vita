pet_schema = {
    "type": "object",
    "required": ["id", "name", "photoUrls", "tags", "status"],
    "properties": {
        "id": {"type": "integer"},
        "category": {
            "type": ["object", "null"],
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"}
            }
        },
        "name": {"type": "string"},
        "photoUrls": {
            "type": "array",
            "items": {"type": ["string", "null"]}  
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                }
            }
        },
        "status": {
            "type": "string",
            "enum": ["available", "pending", "sold"]
        }
    }
}

error_schema = {
    "type": "object",
    "required": ["code", "type", "message"],
    "properties": {
        "code": {"type": "integer"},
        "type": {"type": "string"},
        "message": {"type": "string"}
    }
}