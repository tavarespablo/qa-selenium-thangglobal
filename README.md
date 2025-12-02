# QA Selenium ThangGlobal

## 📌 Project Overview
This repository contains automated test scripts built with **Python + Selenium** to validate workflows on the [Thang Global](https://thangglobal.com) website.  
The goal is to ensure reliability, repeatability, and clear reporting for QA processes.

## 🛠 Technologies
- Python 3.14
- Selenium WebDriver
- Pytest
- Pytest-HTML (for test reports)

## 🚀 Getting Started

### 1. Clone the repository
git clone https://github.com/tavarespablo/qa-selenium-thangglobal.git
cd qa-selenium-thangglobal
### 2. Create and activate virtual environment
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run tests
pytest --html=report.html

## 📂 Project Structure
qa-selenium-thangglobal/
│
├── tests/                # Test cases
├── drivers/              # WebDriver executables (ignored in .gitignore)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation


## 📊 Reports
- Test execution generates an HTML report (report.html) with results and logs.
## 📌 Notes
- Ensure you have the correct WebDriver version installed (ChromeDriver or GeckoDriver).
- The drivers/ folder is ignored in Git to avoid uploading binaries.