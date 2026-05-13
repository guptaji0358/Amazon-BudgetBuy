# 🛒 BudgetBuy

## 🚀 Day 47/100 Python Challenge — Amazon Budget Buy

BudgetBuy is a Python-based smart shopping assistant that helps users check whether a product is within their budget or still too expensive.

Users simply paste an Amazon product URL, enter their target price, and the application automatically checks the current product price.

If the product becomes affordable, BudgetBuy can send an email notification 📧

---

# ✨ Features

- ✅ Amazon product URL tracking
- ✅ Budget comparison system
- ✅ Email alert notifications
- ✅ Colored terminal UI
= ✅ Input validation
- ✅ Error handling
- ✅ Beginner-friendly clean code
- ✅ Real-world automation project

---

# 🛠 Technologies Used

* Python
* Requests
* BeautifulSoup4
* SMTP
* Colorama

---

# 📦 Installation

Install required libraries:

```bash id="8kq5ae"
pip install requests beautifulsoup4 colorama
```

---

# 🚀 Run The Project

```bash id="4x9l7q"
py 47_AMAZON_BUDGET_BUY.py
```

OR

```bash id="s8n7ka"
python 47_AMAZON_BUDGET_BUY.py
```

---

# 🔐 Important Setup Before Running

Open:

```bash id="w6d0lb"
47_AMAZON_BUDGET_BUY.py
```

Find this section:

```python id="9j0m8r"
UserGmail = "YOUR_GMAIL@gmail.com"
UserPassword = "YOUR_APP_PASSWORD"
ReceiverMail = "RECEIVER@gmail.com"
```

Replace with your own email details.

Example:

```python id="a7x3po"
UserGmail = "robinexample@gmail.com"
UserPassword = "abcd efgh ijkl mnop"
ReceiverMail = "myalerts@gmail.com"
```

---

# ⚠️ IMPORTANT

Do NOT use your normal Gmail password.

Google blocks normal passwords for SMTP login.

You must create a **Google App Password** 🔐

---

# 🚀 How To Generate Gmail App Password

## 1️⃣ Open Google Account Settings

Go to your Google Account settings.

---

## 2️⃣ Enable 2-Step Verification

Search for:

```text id="gx7a6q"
2-Step Verification
```

Enable it first.

---

## 3️⃣ Open App Passwords

After enabling 2-Step Verification:

Search:

```text id="n1t6mc"
App Passwords
```

Open it.

---

## 4️⃣ Generate Password

Select:

```text id="3j0z7r"
App → Mail
Device → Windows Computer
```

Click:

```text id="q8f1el"
Generate
```

---

## 5️⃣ Copy Password

Google will generate a password like:

```text id="v7o5qw"
abcd efgh ijkl mnop
```

Paste it inside:

```python id="v9l0bx"
UserPassword = ""
```

---

# 🔒 Security Warning

Never upload your real Gmail credentials to GitHub.

Before pushing your project to GitHub:

Replace credentials with:

```python id="z1x4nk"
UserGmail = ""
UserPassword = ""
ReceiverMail = ""
```

This keeps your account safe 🔐

---

# 🖥 Example Workflow

- 1️⃣ Paste Amazon Product URL
- 2️⃣ Enter your target budget
- 3️⃣ BudgetBuy checks current product price
- 4️⃣ Receive notification if product is affordable 🎉

---

# 🎬 Demo

## Example Product URL

```text id="5x4o7n"
https://files.catbox.moe/0mcmj9.mp4
```

## Example Run

```bash id="4t9m1p"
🛒 AMAZON PRICE TRACKER

🔗 Paste Amazon Product URL:
https://www.amazon.in/dp/B0CHX1W1XY

💰 Enter Your Target Price:
50000

📦 Product:
Apple iPhone 15 (Black, 128 GB)

💰 Current Price:
₹48999

🎉 Product Is Within Your Budget!

📧 Email Alert Sent Successfully!
```

---

# 🧠 Concepts Used

* Web Scraping
* HTTP Requests
* Email Automation
* Exception Handling
* Terminal Styling
* Input Validation
* Real-world Project Structuring

---

# 🌟 Open Source & Developer Contribution

This project was completed by author **Robin Gupta** ❤️

This project is fully open for learning and development purposes.

Other developers are free to:

* Modify the source code
* Upgrade the UI
* Add database support
* Improve scraping accuracy
* Add better notification systems
* Build GUI versions

Developers can also integrate additional shopping platforms such as:

* 🛍️ Flipkart Integration
* 👕 Myntra Integration
* 🛒 Meesho Integration
* 💻 Ajio Integration
* 📦 Multi-platform product comparison

Feel free to build your own upgraded version of BudgetBuy 🚀

---

Made with Python ❤️ by Robin Gupta
