# ai/threat_analyzer.py
def analyze_threat(text):
    """Check if the text has any threats."""
    text = text.lower()  # Make it easy to find words
    # Old rules
    if "http" in text and "urgent" in text:
        return {"type": "phishing", "confidence": 0.9}
    if "proves" in text:
        return {"type": "misinformation", "confidence": 0.8}
    # New rules
    if "fake@" in text or "from:" in text:
        return {"type": "spoofing", "confidence": 0.85}
    if ".exe" in text or "download" in text:
        return {"type": "malware", "confidence": 0.9}
    if "video" in text and ("shocking" in text or "leaked" in text):
        return {"type": "deepfake", "confidence": 0.8}
    if "suspicious login" in text or "verify details" in text:
        return {"type": "social_engineering", "confidence": 0.85}
    if "encrypted" in text or "ransom" in text:
        return {"type": "ransomware", "confidence": 0.9}
    if "keylogger" in text or "recording" in text:
        return {"type": "spyware", "confidence": 0.9}
    if "backdoor" in text or "remote access" in text:
        return {"type": "trojan", "confidence": 0.85}
    if "pop-up" in text or "affiliate" in text:
        return {"type": "adware", "confidence": 0.8}
    if "rootkit" in text or "hide" in text:
        return {"type": "rootkit", "confidence": 0.9}
    if "<script>" in text:
        return {"type": "xss", "confidence": 0.95}
    if "intercepting" in text or "spoofing" in text:
        return {"type": "mitm", "confidence": 0.9}
    return {"type": "safe", "confidence": 0.5}  # If no threats, it’s safe

def recommend_action(analysis):
    """Tell what to do based on the threat."""
    threat_types = analysis["type"]
    if threat_types in ["phishing", "spoofing", "malware", "social_engineering", "trojan", "adware", "xss", "mitm", "rootkit"]:
        return "Please delete this email"
    if threat_types in ["misinformation", "deepfake", "ransomware", "spyware"]:
        return "Please ignore this post"
    return "Safe to proceed"

def process_threat(text, threat_id):
    """Put it all together for each message."""
    analysis = analyze_threat(text)
    recommendation = recommend_action(analysis)
    return {
        "id": threat_id,
        "analysis": analysis,
        "recommendation": recommendation
    }