# ************* header_scanner.py ***********
import requests

# List of important security headers
SECURITY_HEADERS = [
    "X-Frame-Options",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "Strict-Transport-Security"
]

def check_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers

        missing_headers = []

        for header in SECURITY_HEADERS:
            if header not in headers:
                missing_headers.append(header)

        return missing_headers, headers

    except Exception as e:
        print("[-] Error while checking headers:", e)
        return [], {}