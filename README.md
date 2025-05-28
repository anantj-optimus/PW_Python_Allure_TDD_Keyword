# Playwright Python Automation Framework

A simple and scalable Playwright automation framework using Python.

## 🔧 Features

* Playwright with Python
* Page Object Model (POM)
* Data-driven testing with Excel
* Allure reports for test results and screenshots
* Jenkins integration
* Cross-browser support
* Screenshot capture on failure

---

## 📁 Project Structure

```
tdd_pw_framework/
├── tests/                   # Test cases
├── pages/                   # Page object classes
├── utils/                   # Excel reader, logger, etc.
├── data/                    # Test data (Excel files)
├── config.py                # Config file for paths/text
├── conftest.py              # Playwright setup hooks
├── pytest.ini               # Pytest settings
├── requirements.txt         # Python dependencies
└── Jenkinsfile (optional)   # For Jenkins pipelines
```

---

## ▶️ Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/tdd_pw_framework.git
cd tdd_pw_framework
```

### 2. Set Up Virtual Environment (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
npx playwright install --with-deps
```

### 4. Run Tests

```bash
pytest --alluredir=allure-results
```

### 5. View Allure Report

```bash
allure serve allure-results
```

---

## 🧪 Running via Jenkins (Freestyle Job)

1. Clone repo using Git step
2. Run the following batch script as your build step:

```bat
:: 1. Set up Python virtual environment
python -m venv venv
call venv\Scripts\activate

:: 2. Install Python dependencies
pip install -r requirements.txt

:: 3. Install Playwright browsers (Python version)
playwright install

:: 4. Run tests with Allure report
pytest --alluredir=allure-results
```

3. Add "Allure Report" as a post-build action with `allure-results` as the path

---

## 📝 Data-Driven Testing

* Place your Excel file in `data/`
* Update `file_path` in `config.py`
* Add search terms in the Excel rows

---

## 📷 Screenshot on Failure

* Screenshots are saved in the `screenshots/` folder
* Failures with screenshots are attached to Allure reports automatically

---

## ✅ Sample Test Command

```bash
pytest tests/test_google_search.py --alluredir=allure-results
```

---

## 📄 Dependencies

```
pytest
playwright
pytest-playwright
allure-pytest
openpyxl
```

---

## 📬 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## 📃 License

MIT
