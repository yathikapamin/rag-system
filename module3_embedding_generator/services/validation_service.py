def validate_input(data):

    required_fields = [
        "document_id",
        "page_number",
        "content_type",
        "generated_summary"
    ]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing field: {field}")

    if not data["generated_summary"].strip():
        raise ValueError("Generated summary is empty")

    return True