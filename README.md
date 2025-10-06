# SMTP-Config
Secure Python utility for sending emails using SMTP environment configurations.

# 📧 SMTP Config Utility

A simple, production-ready **Python SMTP Email Utility** that securely sends emails using credentials stored in environment variables.

This project demonstrates professional Python coding practices — configuration management, modular design and error handling.

---

## 🚀 Features
- Loads SMTP credentials securely from `.env`
- Sends plain-text emails with TLS encryption
- Provides clear logging and error handling
- Follows clean code and PEP8 style conventions
- Includes unit tests using `unittest.mock`

---

## 🧩 Project Structure

SMTP Config/
├── smtp_utils/
│ ├── init.py
│ └── smtp_configurations.py
├── example_send.py
├── .env.example
├── requirements.txt

---

## ⚙️ Setup and Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/SMTP-Config.git
cd "SMTP Config"

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Create a .env file

Copy from .env.example and replace values:

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password
