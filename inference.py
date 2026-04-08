import requests

BASE_URL = "https://pallavibs0101-viginova-env.hf.space"

print("[START]")

r = requests.post(f"{BASE_URL}/reset")
print("[STEP]", r.json())

r = requests.post(f"{BASE_URL}/step", json={"action": "test"})
print("[STEP]", r.json())

print("[END]")
