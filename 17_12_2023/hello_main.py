import requests

def get_external_data() -> str:
    # Assume this function makes an API call to an external service
    response = requests.get("https://api.example.com/data")
    return (response.text)

def process_external_data() -> str:
    data = get_external_data()
    return f"Processed data: {data}"
