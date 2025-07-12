import re
import tldextract

def detect_phishing(url):
    suspicious_keywords = [
        'login', 'verify', 'update', 'secure', 'account', 'webscr',
        'signin', 'wp', 'dropbox', 'bank', 'confirm', 'validate'
    ]
    bad_tlds = ['.tk', '.ga', '.ml', '.cf', '.gq', '.ru']
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    subdomain = extracted.subdomain

    score = 0

    # Check for IP address in URL
    if re.search(r'http[s]?://\d{1,3}(\.\d{1,3}){3}', url):
        score += 2

    # Too many subdomains
    if subdomain.count('.') > 1:
        score += 1

    # Check for suspicious keywords
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        score += 2

    # Check for bad TLDs
    if any(domain.endswith(tld) for tld in bad_tlds):
        score += 2

    # Check for known brand misspelling
    if re.search(r'paypa1|faceb00k|g00gle|micros0ft|app1e', url.lower()):
        score += 2

    # Final classification
    if score >= 5:
        return "🚨 Likely phishing"
    elif score >= 2:
        return "⚠️ Suspicious"
    else:
        return "✅ Likely safe"

# -------------------------------
# Main execution
# -------------------------------
if __name__ == "__main__":
    print("🛡️ Phishing URL Detector")
    url = input("Enter URL to check: ").strip()
    print("\nResult:", detect_phishing(url))
