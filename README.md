# 🛡️ Astryx
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Security Tool](https://img.shields.io/badge/Type-Web%20Security%20Scanner-red)
![Status](https://img.shields.io/badge/Status-Active-success)

**🚀 Find vulnerabilities before attackers do🚀**

Astryx is an automated **Web Security Scanner** designed to identify common vulnerabilities in web applications.  
The tool performs security analysis on a target website and detects potential weaknesses such as missing security headers, exposed directories, and injection vulnerabilities.

This project is built to demonstrate **practical cybersecurity concepts**, **automated vulnerability detection**, and **secure coding practices**.

---

# 🚀 Features

- 🔍 Scan websites for common security vulnerabilities  
- 🛡️ Detect missing **HTTP Security Headers**  
- 📂 Discover exposed **directories and endpoints**  
- 💉 Identify potential **SQL Injection vulnerabilities**  
- ⚡ Detect basic **Cross-Site Scripting (XSS)** issues  
- 📊 Generate structured **vulnerability scan reports**  
- 🖥️ Simple **command-line interface**

---

# 🧠 How Astryx Works

Astryx performs automated security testing in multiple phases:

1. **Target Validation**
   - Verifies that the target website is reachable.

2. **HTTP Header Analysis**
   - Checks for missing security headers.

3. **Directory Enumeration**
   - Uses a wordlist to discover hidden directories.

4. **Vulnerability Testing**
   - Tests for common injection vulnerabilities.

5. **Report Generation**
   - Compiles detected vulnerabilities into a structured report.

---

# 🏗️ Project Structure

```text
astryx/
│
├── README.md
├── requirements.txt
├── scanner
│ ├── scanner.py
│ ├── scanner_engine.py
│ └── config.py
│
├── modules
│ ├── header_scanner.py
│ ├── directory_scanner.py
│ ├── sqli_scanner.py
│ └── xss_scanner.py
│
├── wordlists
│ └── common_directories.txt
│
├── reports
│ ├── report_generator.py
│ └── report_template.html
│
├── output
│ └── scan_report.html
│
└── docs
├── project_overview.md
├── system_architecture.md
└── functional_requirements.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/astryx.git
cd astryx

Install dependencies:

pip install -r requirements.txt
▶️ Usage

Run the scanner using:

python -m scanner.scanner
Enter url : http://www.example.com

Example output:

Astryx v1.0
Starting Web Security Scan...

[!] Missing Security Headers
 - X-Frame-Options
 - Content-Security-Policy

[!] Directory Found
 - /admin
 - /backup

Scan Completed
📊 Sample Scan Report

Astryx generates a vulnerability report containing:

- Target information

- Detected vulnerabilities

- Severity level

- Security recommendations

Example:

Target: https://example.com

Vulnerabilities Detected:
- Missing Security Headers
- Exposed Directory: /admin

Severity: Medium
```
---
🛠️ Technology Stack

1. Python

2. requests – HTTP requests

3. BeautifulSoup – HTML parsing

4. argparse – CLI interface

5. threading – faster scanning

6. JSON / HTML – report generation

---

🔐 Vulnerabilities Detected

Astryx currently detects:

1. Missing HTTP Security Headers

2. Directory Exposure

3. Basic SQL Injection

4. Reflected Cross-Site Scripting (XSS)

5. Server Information Disclosure

6. Future versions may include:

7. Subdomain discovery

8. Port scanning

9. Technology fingerprinting

10. Advanced vulnerability detection
    
---
📚 Learning Objectives

This project demonstrates practical understanding of:

- Web application security testing

- HTTP protocol analysis

- Automated vulnerability scanning

- Cybersecurity tool development

- Modular software architecture

--- 

⚠️ Disclaimer

Astryx is developed for educational and ethical security testing purposes only.

Do not use this tool on systems or websites without proper authorization.

---
🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you'd like to contribute:

- Fork the repository

- Create a new branch

- Submit a pull request

---
📄 License

This project is licensed under the MIT License.
---
👩‍💻 Author

Sakshi Singh
Cybersecurity Enthusiast | Software Developer

https://www.linkedin.com/in/sakshi-amit-singh/




