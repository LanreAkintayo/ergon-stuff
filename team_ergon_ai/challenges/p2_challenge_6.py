import requests

def call_api(url: str, payload: dict= None):
    try:
        if payload == None:
            response = requests.get(url, timeout=5)
            return response.json()
        else:
            response = requests.post(url, json=payload, timeout=5)
            if response.status_code == 200:
                return response.json()
            else:
                return {
                    "error": f"Server error {response.status_code}"
                }
    except requests.exceptions.ConnectionError:
        return {
            "error": "Connection failed! The server is offline."
        }
        

online_data = call_api("https://httpbin.org/json")
print(online_data["slideshow"]["title"])
print(online_data["slideshow"]["author"])


# Passing a payload
my_payload = {"well_name": "Bonga-01", "porosity": 0.24}
post_result = call_api("https://httpbin.org/post", payload=my_payload)
print(post_result["json"])


# For offline
offline_result = call_api("http://localhost:11434")
print(offline_result)
