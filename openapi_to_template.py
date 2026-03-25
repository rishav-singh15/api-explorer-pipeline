import requests
import json

OPENAPI_URL = "https://api.apidash.dev/openapi.json"
BASE_URL = "https://api.apidash.dev"

CATEGORY_RULES = {
    "AI": ["ai", "openai", "anthropic", "gemini", "llm"],
    "Finance": ["finance", "payment", "bank", "currency"],
    "Weather": ["weather", "forecast", "climate"],
    "Developer Tools": ["convert", "parse", "format"],
}

def fetch_openapi(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print("Error fetching OpenAPI:", e)
        return None

def extract_endpoints(data):
    paths = data.get("paths", {})
    endpoints = []

    for path, methods in paths.items():
        for method, details in methods.items():
            endpoints.append({
                "path": path,
                "method": method.upper(),
                "tags": details.get("tags", [])
            })

    return endpoints

def infer_category(api_name, tags, paths):
    signal = " ".join([
        api_name.lower(),
        " ".join(tags).lower(),
        " ".join(paths).lower()
    ])

    for category, keywords in CATEGORY_RULES.items():
        for keyword in keywords:
            if keyword in signal:
                return category

    return "General"

def build_template(data, endpoints):
    info = data.get("info", {})

    all_tags = list(set(tag for ep in endpoints for tag in ep["tags"]))
    all_paths = [ep["path"] for ep in endpoints]

    template = {
        "info": {
            "name": info.get("title", "Unknown API"),
            "description": info.get("description", "")
        },
        "category": infer_category(info.get("title", ""), all_tags, all_paths),
        "requests": []
    }

    for ep in endpoints[:5]:
        template["requests"].append({
            "method": ep["method"],
            "url": BASE_URL + ep["path"],
            "headers": {},
            "body": {}
        })

    return template

def save_template(template):
    with open("sample_output.json", "w") as f:
        json.dump(template, f, indent=2)

def main():
    data = fetch_openapi(OPENAPI_URL)

    if not data:
        print("Failed to fetch API")
        return

    endpoints = extract_endpoints(data)
    template = build_template(data, endpoints)

    save_template(template)
    print("PoC completed: sample_output.json generated")

if __name__ == "__main__":
    main()