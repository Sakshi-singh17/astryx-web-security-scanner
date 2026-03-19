# ************ directory_scanner.py ***********
import requests
from concurrent.futures import ThreadPoolExecutor


def check_path(url, path):
    full_url = f"{url}/{path}"
    print(f"Scanning: {full_url}")

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(full_url, headers=headers, timeout=5)
        status=response.status_code
        print(f"{full_url} -> {response.status_code}")

        if status == 200 and ("text/html" not in response.headers.get("Content-Type", "") or len(response.text) < 10000):
            return ("FOUND", f"{full_url} (Status: {status})")

        elif status == 301 or status == 302:
            return ("REDIRECT", f"{full_url} (Status: {status})")

        elif status == 401:
            return ("UNAUTHORIZED", f"{full_url} (Status: {status})")

        elif status == 403:
            return ("FORBIDDEN", f"{full_url} (Status: {status})")

        elif status == 500:
            return ("SERVER_ERROR", f"{full_url} (Status: {status})")

        elif status == 503:
            return ("SERVICE_UNAVAILABLE", f"{full_url} (Status: {status})")
    except requests.exceptions.RequestException:
        print(f"[ERROR] Could not connect to {full_url}")
        return None



def scan_directories(url, wordlist_path="wordlists/common.txt"):
    print("\n[+] Starting Multithreaded Directory Scan...\n")
    found = []
    forbidden = []
    redirects = []
    unauthorized = []
    server_errors = []
    service_unavailable = []    


    try:
        with open(wordlist_path, "r") as file:
            paths = file.read().splitlines()

        with ThreadPoolExecutor(max_workers=5) as executor:
            results = executor.map(lambda path: check_path(url, path), paths)

            for result in results:
                if result:
                    status, msg = result

                    print(msg)  # terminal output

                    if status == "FOUND":
                        found.append(msg)
                    elif status == "FORBIDDEN":
                        forbidden.append(msg)
                    elif status == "REDIRECT":
                        redirects.append(msg)
                    elif status == "UNAUTHORIZED":
                        unauthorized.append(msg)
                    elif status == "SERVER_ERROR":
                        server_errors.append(msg)
                    elif status == "SERVICE_UNAVAILABLE":
                        service_unavailable.append(msg)

    except FileNotFoundError:
        print("[ERROR] Wordlist file not found!")

    return {
    "found": found,
    "forbidden": forbidden,
    "redirects": redirects,
    "unauthorized": unauthorized,
    "server_errors": server_errors,
    "service_unavailable": service_unavailable
}