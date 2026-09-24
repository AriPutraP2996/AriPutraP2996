from __future__ import annotations


def normalize_records(payload) -> list[dict]:
    if not isinstance(payload, list):
        raise ValueError("Expected a JSON array.")

    output = []
    for item in payload:
        if not isinstance(item, dict):
            raise ValueError("Each record must be an object.")
        if "id" not in item or "name" not in item:
            raise ValueError("Each record requires 'id' and 'name'.")
        output.append({
            "id": int(item["id"]),
            "name": str(item["name"]).strip(),
            "email": str(item.get("email", "")).strip().lower(),
        })
    return output
