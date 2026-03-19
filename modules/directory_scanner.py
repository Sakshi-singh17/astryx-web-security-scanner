import requests

def scan_directories(url, wordlist_path="wordlists/common.txt"):
    print("\n[+] Starting Wordlist-Based Directory Scan...\n")

    try:
        with open(wordlist_path, "r") as file:
            paths = file.read().splitlines()

        for path in paths:
            full_url = f"{url}/{path}"

            try:
                response = requests.get(full_url)

                if response.status_code == 200:
                    print(f"[FOUND] {full_url} (Status: {response.status_code})")

                elif response.status_code == 403:
                    print(f"[FORBIDDEN] {full_url} (Status: {response.status_code})")

            except requests.exceptions.RequestException:
                pass

    except FileNotFoundError:
        print("[ERROR] Wordlist file not found!")