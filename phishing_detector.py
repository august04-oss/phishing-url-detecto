import re
import tldextract

# Suspicious keywords commonly found in phishing URLs
SUSPICIOUS_KEYWORDS = [
    "login", "verify", "account", "secure", "update",
    "signin", "submit", "banking", "password", "confirm"
]

def is_ip_address(url):
    """Detect if URL is using an IP instead of domain name"""
    return bool(re.match(r'^https?://\d{1,3}(\.\d{1,3}){3}', url))

def contains_keywords(url):
    """Check if URL contains known phishing keywords"""
    return any(keyword in url.lower() for keyword in SUSPICIOUS_KEYWORDS)

def has_many_subdomains(url):
    """Check if URL has more than 2 subdomains (unusual)"""
    parts = tldextract.extract(url)
    subdomain = parts.subdomain
    return len([s for s in subdomain.split('.') if s]) > 2

def is_suspicious_length(url):
    """Check if URL is unusually long"""
    return len(url) > 75

def detect_phishing(url):
    """Main detection logic"""
    score = 0

    if is_ip_address(url):
        print("⚠️ Uses IP address instead of domain")
        score += 2

    if contains_keywords(url):
        print("⚠️ Contains suspicious keywords")
        score += 2

    if has_many_subdomains(url):
        print("⚠️ Too many subdomains")
        score += 1

    if is_suspicious_length(url):
        print("⚠️ URL is too long")
        score += 1

    print("\n🔍 Final Analysis:")
    if score >= 5:
        return "❌ Likely PHISHING"
    elif score >= 3:
        return "⚠️ Suspicious"
    else:
        return "✅ Looks safe"

if __name__ == "__main__":
    print("🛡️ Phishing URL Detector")
    user_url = input("Enter URL to scan: ").strip()
    result = detect_phishing(user_url)
    print(f"\nResult: {result}")
