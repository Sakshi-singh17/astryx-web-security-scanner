import requests

def scan_directories(url):
    print("\n[+] Starting Directory Scan...\n")

    common_paths = [
        "admin",
        "login",
        "dashboard",
        "backup",
        "api",
        "test"
    ]

    for path in common_paths:
        full_url = f"{url}/{path}"

        try:
            response = requests.get(full_url)

            if response.status_code == 200:
                print(f"[FOUND] {full_url} (Status: {response.status_code})")

            elif response.status_code == 403:
                print(f"[FORBIDDEN] {full_url} (Status: {response.status_code})")

        except requests.exceptions.RequestException:
            pass