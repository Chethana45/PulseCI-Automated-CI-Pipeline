# PulseCI – Automated CI Pipeline

[![PulseCI - Automated CI Pipeline](https://github.com/YOUR_USERNAME/PulseCI/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/PulseCI/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Tested with Pytest](https://img.shields.io/badge/tested_with-pytest-yellow.svg)](https://docs.pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A beginner-friendly DevOps Continuous Integration (CI) project that automates dependency management, application verification, and test execution using **GitHub Actions**.

---

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Solution](#-solution)
- [Architecture Diagram](#-architecture-diagram)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Local Setup & Installation](#-local-setup--installation)
  - [Prerequisites](#prerequisites)
  - [Option A: WSL2 Ubuntu (Recommended)](#option-a-wsl2-ubuntu-recommended)
  - [Option B: Windows PowerShell](#option-b-windows-powershell)
- [Running the Application](#-running-the-application)
- [Running Automated Tests](#-running-automated-tests)
- [How GitHub Actions Works](#-how-github-actions-works)
- [Pushing to GitHub & Triggering the Pipeline](#-pushing-to-github--triggering-the-pipeline)
- [Screenshots & Verification](#-screenshots--verification)
- [Future Enhancements](#-future-enhancements)

---

## 📖 Project Overview

**PulseCI** demonstrates the foundational building block of modern DevOps: **Automated Continuous Integration (CI)**.

Whenever a developer pushes new code or opens a Pull Request against the `main` branch, a GitHub Actions runner automatically:
1. Provisions a clean Ubuntu virtual machine.
2. Checks out the repository code.
3. Configures the Python 3.11 runtime environment.
4. Installs required project dependencies.
5. Executes the core application logic.
6. Runs a suite of unit, boundary, and error-handling tests using `pytest`.
7. Generates a clear pass/fail status report.

---

## 🛑 Problem Statement

In traditional software development without CI:
- Developers test code only on their local machines ("*It works on my machine!*").
- Broken code, missing dependencies, or failing regression tests are frequently merged into production branches.
- Manual testing before each release is slow, repetitive, and error-prone.
- Teams lack real-time visibility into the health and stability of the codebase.

---

## 💡 Solution

**PulseCI** introduces an automated feedback loop:
- **Instant Feedback:** Every code change pushed to GitHub is validated in seconds.
- **Consistent Testing Environment:** Every build runs in an isolated, standardized container/runner, eliminating environment discrepancies.
- **Quality Gate:** Failing tests immediately block bad code from entering the repository.
- **Zero Manual Effort:** Testing and verification require zero manual intervention from developers.

---

## 🏗️ Architecture Diagram

```mermaid
flowchart TD
    A[Developer edits code locally] -->|git push / pull request| B[GitHub Repository (main branch)]
    B -->|Webhook Trigger| C[GitHub Actions Runner (ubuntu-latest)]
    
    subgraph CI Pipeline Execution
        C --> D[Step 1: actions/checkout@v4]
        D --> E[Step 2: actions/setup-python@v5]
        E --> F[Step 3: Install dependencies via pip]
        F --> G[Step 4: Execute python app.py]
        G --> H[Step 5: Run pytest -v test_app.py]
    end
    
    H -->|All Tests Pass| I[Green Build / Step Summary Published]
    H -->|Any Test Fails| J[Red Build / Merge Blocked & Alert]
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
| :--- | :--- |
| **Python 3.11+** | Application programming language |
| **Pytest** | Testing framework for unit and boundary tests |
| **Git** | Distributed version control system |
| **GitHub** | Remote repository hosting and collaboration |
| **GitHub Actions** | Cloud-native Continuous Integration (CI) platform |
| **YAML** | Declarative pipeline configuration format |

---

## 📂 Project Structure

```
PulseCI/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI workflow definition
├── app.py                  # Core pricing and discount calculation module
├── test_app.py             # Pytest suite (normal, boundary, and invalid tests)
├── requirements.txt        # Project dependencies (pytest)
├── .gitignore              # Files and folders ignored by Git
└── README.md               # Project documentation and guide
```

### File Breakdown:
- **`app.py`**: Contains core pricing calculations (`calculate_discount`, `calculate_total_price`, and `validate_number`). Includes an executable `main()` demo.
- **`test_app.py`**: Automated test suite containing 8 test cases covering standard inputs, boundary values (0%, 100%, single item), and invalid inputs (negative prices, strings, invalid ranges).
- **`requirements.txt`**: Specifies test dependencies (`pytest>=7.4.0`).
- **`.gitignore`**: Prevents Python cache (`__pycache__`), virtual environments (`.venv`), and test artifacts from polluting Git.
- **`.github/workflows/ci.yml`**: The CI configuration file instructing GitHub Actions what steps to run on every push and PR.

---

## 💻 Local Setup & Installation

Follow these simple steps to run PulseCI on your local machine.

### Prerequisites
Make sure you have either **WSL2 (Ubuntu)** or **Windows with Python 3** installed.

---

### Option A: WSL2 Ubuntu (Recommended)

1. **Open your WSL2 terminal** and navigate to your project directory:
   ```bash
   cd "/mnt/c/Users/cheth/OneDrive/Desktop/PulseCI – Automated CI Pipeline"
   ```

2. **Verify Python & Pip are installed:**
   ```bash
   python3 --version
   pip3 --version
   ```
   *(If not installed: `sudo apt update && sudo apt install -y python3 python3-pip python3-venv`)*

3. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. **Install project dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

### Option B: Windows PowerShell

1. **Open PowerShell** in the project folder:
   ```powershell
   cd "c:\Users\cheth\OneDrive\Desktop\PulseCI – Automated CI Pipeline"
   ```

2. **Create and activate a virtual environment:**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   *(If script execution is restricted: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

3. **Install project dependencies:**
   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## 🚀 Running the Application

To execute the application and see the pricing engine in action:

**WSL2 Ubuntu:**
```bash
python3 app.py
```

**Windows PowerShell:**
```powershell
python app.py
```

**Expected Output:**
```text
==================================================
 PulseCI E-Commerce Pricing Engine 
==================================================
Item Unit Price    : $49.99
Quantity           : 3
Discount Rate      : 10.0%
Tax Rate           : 8.5%
--------------------------------------------------
Final Total Price  : $146.44
==================================================
[SUCCESS] Application executed cleanly.
```

---

## 🧪 Running Automated Tests

Run the Pytest suite locally to verify all test cases:

```bash
pytest -v
```

**Expected Output:**
```text
============================= test session starts ==============================
collected 8 items

test_app.py::test_calculate_discount_normal PASSED                      [ 12%]
test_app.py::test_calculate_total_price_normal PASSED                   [ 25%]
test_app.py::test_calculate_discount_zero_percent PASSED                [ 37%]
test_app.py::test_calculate_discount_full_hundred_percent PASSED        [ 50%]
test_app.py::test_calculate_total_price_minimum_quantity_and_zero_tax PASSED [ 62%]
test_app.py::test_calculate_discount_exceeding_max_percentage PASSED    [ 75%]
test_app.py::test_calculate_total_price_negative_unit_price PASSED     [ 87%]
test_app.py::test_calculate_total_price_zero_quantity PASSED            [100%]

============================== 8 passed in 0.05s ===============================
```

### Test Case Overview:
1. `test_calculate_discount_normal`: Normal 20% discount calculation.
2. `test_calculate_total_price_normal`: Full pricing flow with discount and sales tax.
3. `test_calculate_discount_zero_percent`: Boundary test verifying 0% discount equals $0.
4. `test_calculate_discount_full_hundred_percent`: Boundary test verifying 100% discount covers full cost.
5. `test_calculate_total_price_minimum_quantity_and_zero_tax`: Boundary test with quantity 1 and zero tax.
6. `test_calculate_discount_exceeding_max_percentage`: Error test asserting rejection of > 100% discount.
7. `test_calculate_total_price_negative_unit_price`: Error test asserting rejection of negative prices.
8. `test_calculate_total_price_zero_quantity`: Error test asserting quantity cannot be 0.

---

## ⚙️ How GitHub Actions Works

The automated pipeline is defined in `.github/workflows/ci.yml`. Here is how each component works:

1. **Triggers (`on:`):**
   - Listens for `push` events to `main`.
   - Listens for `pull_request` events targeting `main`.
2. **Runner (`runs-on: ubuntu-latest`):**
   - GitHub provisions a fresh, secure Ubuntu Linux virtual environment in the cloud.
3. **Checkout (`actions/checkout@v4`):**
   - Clones your repository into the runner's workspace.
4. **Python Setup (`actions/setup-python@v5`):**
   - Installs the specified Python version (`3.11`) and enables pip dependency caching.
5. **Dependency Installation (`pip install`):**
   - Upgrades pip and installs all packages listed in `requirements.txt`.
6. **Execution & Pytest:**
   - Runs `python app.py` to ensure the program executes without crashes.
   - Runs `pytest -v` to validate all business rules and edge cases.
7. **Job Status & Summary:**
   - If all steps exit with code `0`, GitHub marks the workflow with a green checkmark (`✔`).
   - If any step fails (exit code != 0), the workflow turns red (`✖`) and stops, alerting the author.

---

## 📤 Pushing to GitHub & Triggering the Pipeline

Follow these steps to publish your project and watch your pipeline run live:

### 1. Initialize Git and Commit
```bash
git init
git add .
git commit -m "feat: initial PulseCI setup with app, tests, and CI workflow"
```

### 2. Rename Default Branch to `main`
```bash
git branch -M main
```

### 3. Create a GitHub Repository
1. Go to [GitHub.com](https://github.com) and click **New Repository**.
2. Name it **`PulseCI`** (or your preferred name).
3. Leave "Initialize with README" **unchecked** (we already have one).
4. Click **Create repository**.

### 4. Link Remote and Push
```bash
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/PulseCI.git
git push -u origin main
```

### 5. Verify the Workflow on GitHub
1. Navigate to your repository on GitHub.
2. Click on the **Actions** tab at the top.
3. You will see the **`PulseCI - Automated CI Pipeline`** workflow running.
4. Click on the workflow run to view the live logs for each step (**Checkout**, **Install dependencies**, **Execute application**, and **Run Pytest**).
5. When complete, a green checkmark will appear!

---

## 📸 Screenshots & Verification

> Once your workflow completes on GitHub, take screenshots of your run and place them in an `assets/` or `docs/` folder, or embed them directly here.

| Workflow Run Overview | Pytest Execution in GitHub Actions |
| :---: | :---: |
| *[Add screenshot of GitHub Actions list with green checkmark]* | *[Add screenshot of expanded Pytest step showing 8 passed tests]* |

---

## 🔮 Future Enhancements

As you grow your DevOps skills, here are great next steps to extend this project:
- [ ] **Code Linting & Formatting:** Add `ruff` or `flake8` and `black` to check code quality in CI.
- [ ] **Test Coverage Reports:** Integrate `pytest-cov` and upload coverage reports to [Codecov](https://codecov.io/).
- [ ] **Matrix Builds:** Test across multiple Python versions (`3.10`, `3.11`, `3.12`) simultaneously.
- [ ] **Security Scanning:** Add `bandit` or `safety` to scan for known vulnerabilities in Python dependencies.
- [ ] **ChatOps Notifications:** Send a Slack or Discord webhook alert whenever a build fails.

---

## 📄 License
This project is open-source under the [MIT License](LICENSE).
