
question_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "version": "1.0.0",
  "properties": {
    "question": {"type": "string"},
    "answer": {"type": "string"},
    "justification": {"type": "string"},
    "confidence_score": {"type": "integer"}
  },
  "required": ["question", "answer", "justification", "confidence_score"],
}

schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "version": "1.0.0",
    "properties": {
        "general_info": {
            "type": "object",
            "properties": {
                "chief_complaint": {"type": "string"},
                "treatment_plan": {"type": "string"},
                "allergies": {"type": "string"},
                "preexisting_medications": {
                    "type": "string",
                },
                "meta": {
                    "type": "object",
                    "properties": {
                        "risk_assessment": {"type": "string"},
                        "treatment_assessment": {"type": "string"}
                    },
                    "required": ["risk_assessment", "treatment_assessment"]
                }
            },
            "required": [
                "chief_complaint",
                "treatment_plan",
                "allergies",
                "preexisting_medications",
                "meta"
            ]
        },
        "questions": {
            "type": "array",
            "items": question_schema
        },
        "treatment_plan_appropriate": {"type": "string"}
    },
    "required": ["general_info", "questions", "treatment_plan_appropriate"]
}


# Initialize objects based on schema
def initialize_object_from_schema(schema):
    if "type" not in schema:
        return None

    if schema["type"] == "object":
        obj = {}
        for prop, prop_schema in schema.get("properties", {}).items():
            obj[prop] = initialize_object_from_schema(prop_schema)
        return obj

    elif schema["type"] == "array":
        return []

    elif schema["type"] == "string":
        return ""

    elif schema["type"] == "integer":
        return 0

    elif schema["type"] == "number":
        return 0.0

    elif schema["type"] == "boolean":
        return False

    elif schema["type"] == "null":
        return None

    return None
