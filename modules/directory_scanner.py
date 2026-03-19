import requests
from concurrent.futures import ThreadPoolExecutor

def check_path(url, path):
    full_url = f"{url}/{path}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(full_url, headers=headers, timeout=5)

        if response.status_code == 200:
            print(f"[FOUND] {full_url} (Status: {response.status_code})")

        elif response.status_code == 403:
            print(f"[FORBIDDEN] {full_url} (Status: {response.status_code})")

    except requests.exceptions.RequestException:
        pass


def scan_directories(url, wordlist_path="wordlists/common.txt"):
    print("\n[+] Starting Multithreaded Directory Scan...\n")

    try:
        with open(wordlist_path, "r") as file:
            paths = file.read().splitlines()

        # 🔥 Multithreading starts here
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(lambda path: check_path(url, path), paths)

    except FileNotFoundError:
        print("[ERROR] Wordlist file not found!")