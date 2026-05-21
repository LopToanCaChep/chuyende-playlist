import hashlib, time, requests, os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")
cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME")
api_key    = os.getenv("CLOUDINARY_API_KEY")
api_secret = os.getenv("CLOUDINARY_API_SECRET")

timestamp = str(int(time.time()))
params = f"folder=chuyende_assets&timestamp={timestamp}"
signature = hashlib.sha1((params + api_secret).encode()).hexdigest()

with open(r"Pic\_[TCC]Mascot_4.png", "rb") as f:
    resp = requests.post(
        f"https://api.cloudinary.com/v1_1/{cloud_name}/image/upload",
        data={
            "api_key": api_key,
            "timestamp": timestamp,
            "signature": signature,
            "folder": "chuyende_assets",
        },
        files={"file": f}
    )

data = resp.json()
if "secure_url" in data:
    print("SUCCESS:", data["secure_url"])
else:
    print("ERROR:", data)
