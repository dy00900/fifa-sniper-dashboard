import json, subprocess
from datetime import datetime

# Test sample payload - we can wire this directly to your sniper output file next
data = {
    "updated": datetime.now().strftime("%b %d, %I:%M %p"),
    "picks": [
        {
            "league": "Live System Test",
            "match": "Arsenal vs Chelsea",
            "market": "Over 2.5 Goals",
            "odds": "1.95",
            "prob": "56.4%",
            "edge": "+4.8%"
        }
    ]
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

subprocess.run(["git", "add", "index.html", "data.json"], check=True)
subprocess.run(["git", "commit", "-m", "Auto-sync ledger picks"], check=False)
subprocess.run(["git", "push", "origin", "main"], check=True)
print("✅ Live dashboard updated on Vercel!")
