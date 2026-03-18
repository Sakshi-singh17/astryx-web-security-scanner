from modules.header_scanner import check_headers

def start_scan(url):
    print("\n🛡️ Astryx v1.0")
    print("Scanning:", url)
    print("-" * 40)

    missing_headers, headers = check_headers(url)

    # Display Results
    if missing_headers:
        print("[!] Missing Security Headers:")
        for h in missing_headers:
            print(" -", h)
    else:
        print("[+] All important security headers are present")

    # Server Info Disclosure
    if "Server" in headers:
        print("\n[!] Server Information Disclosure:")
        print(" -", headers["Server"])

    print("\nScan Completed ✅")

if __name__ == "__main__":
    target = input("Enter target URL: ")
    start_scan(target)