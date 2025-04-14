# ai/test_analyzer.py
from threat_analyzer import process_threat

# Test some messages from threats.json
threats = [
    {"id": 1, "text": "Urgent! Click http://free-gift.com to claim your $500 reward!"},
    {"id": 4, "text": "Scientists confirm the Earth is flat!"},
    {"id": 10, "text": "From: admin@paypal.com (really fake@phishmail.com) — Update your payment info."},
    {"id": 7, "text": "Good morning! Team meeting is at 10 AM."}
]

# See what the AI says
for t in threats:
    result = process_threat(t["text"], t["id"])
    print(f"ID: {result['id']}")
    print(f"What it found: {result['analysis']}")
    print(f"What to do: {result['recommendation']}\n")