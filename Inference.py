
import requests

BASE_URL = "https://pallavibs0101-viginova-env.hf.space"

print("[START]")

try:
    # RESET
    r = requests.post(f"{BASE_URL}/reset")
    print("[STEP] Reset:", r.json())

    # STEP
    action = {"action": "emergency"}
    r = requests.post(f"{BASE_URL}/step", json=action)
    print("[STEP] Action:", r.json())

    print("[END]")

except Exception as e:
    print("[ERROR]", str(e))
