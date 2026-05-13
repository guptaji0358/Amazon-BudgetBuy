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
- ✅ Input validation
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

```bash id="m0i7jw"
pip install requests beautifulsoup4 colorama
```

---

# 🚀 Run The Project

```bash id="6f5jwr"
py 47_AMAZON_BUDGET_BUY.py
```

OR

```bash id="8v9h7p"
python 47_AMAZON_BUDGET_BUY.py
```

---

# 🔐 Important Setup Before Running

Open:

```bash id="zyjlwm"
47_AMAZON_BUDGET_BUY.py
```

Find this section:

```python id="c1a0dt"
UserGmail = "YOUR_GMAIL@gmail.com"
UserPassword = "YOUR_APP_PASSWORD"
ReceiverMail = "RECEIVER@gmail.com"
```

Replace with your own email details.

Example:

```python id="r0ahcz"
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

```text id="1em3pr"
2-Step Verification
```

Enable it first.

---

## 3️⃣ Open App Passwords

After enabling 2-Step Verification:

Search:

```text id="k7l8c6"
App Passwords
```

Open it.

---

## 4️⃣ Generate Password

Select:

```text id="fw0rq9"
App → Mail
Device → Windows Computer
```

Click:

```text id="13dc0g"
Generate
```

---

## 5️⃣ Copy Password

Google will generate a password like:

```text id="l2g2lx"
abcd efgh ijkl mnop
```

Paste it inside:

```python id="cxf7pu"
UserPassword = ""
```

---

# 🔒 Security Warning

Never upload your real Gmail credentials to GitHub.

Before pushing your project to GitHub:

Replace credentials with:

```python id="qf1p91"
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

# 📸 Preview

```bash id="ay7l0g"
🛒 AMAZON PRICE TRACKER

🔗 Paste Amazon Product URL:
https://amazon.in/...

💰 Enter Your Target Price:
50000

📦 Product:
Apple iPhone 15

💰 Current Price:
₹48999

🎉 Product Is Within Your Budget!
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
