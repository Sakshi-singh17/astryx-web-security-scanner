# *********** scanner.py ***********
from modules.header_scanner import check_headers
from modules.directory_scanner import scan_directories
from reports.report_generator import save_report



def start_scan(url):
    print("\n🛡️ Astryx v1.0")
    print("Scanning:", url)
    print("-" * 40)

    results = {
        "Missing Headers": [],
        "Server Info": [],
        "Directories Found": []
    }

    missing_headers, headers = check_headers(url)

    # Display Results
    if missing_headers:
        print("[!] Missing Security Headers:")
        for h in missing_headers:
            print(" -", h)
            results["Missing Headers"].append(h)
    else:
        print("\n[+] All important security headers are present")

    # Server Info Disclosure
    if "Server" in headers:
        print("\n[!] Server Information Disclosure:")
        print(" -", headers["Server"])
        results["Server Info"].append(headers["Server"])

    #  Directory Scan 
    dir_results = scan_directories(url)
    results["Directories Found"] = dir_results["found"]
    results["Forbidden Directories"] = dir_results["forbidden"]
    results["Redirects"] = dir_results["redirects"]
    results["Unauthorized"] = dir_results["unauthorized"]
    results["Server Errors"] = dir_results["server_errors"]
    results["Service Unavailable"] = dir_results["service_unavailable"]

    # Save Report
    save_report(results)


    print("\nScan Completed ✅")

if __name__ == "__main__":
    target = input("Enter target URL: ")
    start_scan(target)