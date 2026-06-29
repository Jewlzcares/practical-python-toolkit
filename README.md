# 🐍 Python Automation Toolkit

A production-style, beginner-friendly CLI toolkit for real-world file automation and system organization.

This project is designed to help me learn Python by building **practical automation tools** while developing clean software engineering habits.

It focuses on modular architecture, safe file operations, and real CLI-based workflows similar to professional tooling.

---

## Purpose of this Project

This repository is not just a learning exercise — it is a structured Python toolkit designed to:

- Teach Python through real automation use cases
- Simulate real-world CLI tools used in software engineering
- Build confidence in working with file systems and scripts
- Develop clean, modular, maintainable code habits
- Serve as a personal automation toolkit for daily tasks

---

##  Core Principles

This project follows professional development principles:

- **Modular Design** – each tool is independent and reusable
- **CLI-First Architecture** – everything runs via command line
- **Safety by Default** – destructive actions require confirmation
- **Dry-Run Mode** – preview changes before execution
- **Windows-Compatible Paths** – uses `pathlib` everywhere
- **Readable Code** – beginner-friendly but structured like production code

---

## Project Structure

```text
practical-python-toolkit/
│
├── main.py                 # CLI entry point
├── README.md               # Documentation
│
├── scripts/
│   ├── automation/         # File automation tools
│   ├── data_tools/         # Data utilities
│   └── misc/               # Experimental tools
│
├── utils/                  # Shared helper functions (future)
└── tests/                  # Unit tests (future)
```

---

## 🚀 Getting Started

### 1. Check Python Installation

```bash
python --version
```

or

```bash
py --version
```

---

### 2. Install Python (if needed)

Download from:

https://www.python.org/downloads/

⚠️ Make sure to enable:
- **Add Python to PATH**

---

### 3. Clone Repository

#### Option A – IDE (Recommended)

- Open IDE → “Get from VCS”
- Paste repository URL
- Clone project

#### Option B – Terminal

```bash
git clone https://github.com/Jewlzcares/practical-python-toolkit.git
cd practical-python-toolkit
```

---

### 4. Run the Project

```bash
python main.py
```

---

## Learning Focus

This project helps you understand:

- Python file handling (`pathlib`, `os`)
- CLI development (`argparse`)
- Modular software architecture
- Safe automation patterns
- Real-world scripting workflows

---

## 🔒 Safety System

All tools in this project follow safe execution rules:

- No accidental file deletion
- Dry-run mode before execution
- Explicit confirmation for destructive actions
- Transparent operation logging
