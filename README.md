# 🛡️ Phishing URL Detector

A simple Python-based tool that detects potentially malicious or phishing URLs using basic rules like suspicious keywords, IP-based domains, excessive subdomains, and long URLs. Designed for students, cybersecurity beginners, or anyone who wants to quickly evaluate the safety of a URL.

---

## 🚀 Features

- 🔍 **Keyword detection** — Checks for phishing-related words like `login`, `verify`, `account`, etc.
- 🌐 **IP address check** — Warns if a URL uses an IP address instead of a domain
- 🧬 **Subdomain analysis** — Flags URLs with too many subdomains (used to spoof trusted domains)
- 📏 **Length check** — Alerts if the URL is unusually long (over 75 characters)
- ✅ **Easy to run** — No complex setup or machine learning needed

---

## 📂 Project Structure

phishing-url-detector/
├── phishing_detector.py # Main Python script
├── requirements.txt # Python dependencies
└── README.md # Project info


---

## 🧑‍💻 Installation

1. Clone this repository:

```bash
git clone https://github.com/YOUR_USERNAME/phishing-url-detector.git
cd phishing-url-detector

Example:

   🛡️ Phishing URL Detector
Enter URL to scan: http://secure-paypa1.com/verify/account

⚠️ Contains suspicious keywords
⚠️ Too many subdomains

🔍 Final Analysis:
❌ Likely PHISHING
