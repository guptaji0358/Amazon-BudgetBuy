<div align="center">

<!-- TOP GRAPHIC BANNER -->
<a href="https://github.com/guptaji0358/Amazon-BudgetBuy">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=🛒%20Amazon%20BudgetBuy&fontSize=42&fontColor=ffffff&animation=twinkling&fontAlignY=38" width="100%" alt="Header Banner" />
</a>

<h3><code>DAY 47 / 100 DAYS OF CODE</code></h3>
<p><b>A Multi-Platform Price Tracker with Seller Authenticity Checks & Automated Email Alerts Built in Python</b></p>

<!-- ACTION BUTTONS -->
<p>
<a href="#-live-demo">
<img src="https://img.shields.io/badge/▶_Watch_Demo-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch Demo"/>
</a>
<a href="#-quick-start">
<img src="https://img.shields.io/badge/⚡_Quick_Start-238636?style=for-the-badge&logo=rocket&logoColor=white" alt="Quick Start"/>
</a>
<a href="https://github.com/guptaji0358/Amazon-BudgetBuy/stargazers">
<img src="https://img.shields.io/badge/⭐_Star_Repository-E3B341?style=for-the-badge&logo=github&logoColor=black" alt="Star Repo"/>
</a>
</p>

<!-- TECH BADGES -->
<p>
<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/BeautifulSoup-4-3776AB?style=for-the-badge&logo=pypi&logoColor=white" alt="BeautifulSoup" />
<img src="https://img.shields.io/badge/SMTP-Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail SMTP" />
<img src="https://img.shields.io/badge/ChatGPT-4o-742774?style=for-the-badge&logo=openai&logoColor=white" alt="ChatGPT" />
<img src="https://img.shields.io/badge/License-MIT-0052CC?style=for-the-badge" alt="License" />
</p>

</div>

<br />

<!-- KEY FEATURES GRID -->
<table width="100%">
<tr>
<td align="center" colspan="2" bgcolor="#0d1117">
<h2>✨ Key Capabilities & Features (v2.0)</h2>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h4>🌐 Multi-Platform Scraping</h4>
<p>Dedicated scrapers for <b>Amazon, Flipkart and Myntra</b>, plus a heuristic <b>Generic scraper</b> that auto-detects title, price and seller on any other store. The right scraper is picked from the URL.</p>
</td>
<td width="50%" valign="top">
<h4>💰 Budget Comparison Engine</h4>
<p>Compares extracted current pricing against user-defined target thresholds with clean data sanitization and mathematical validation.</p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h4>📧 Configurable Email Alerts</h4>
<p>Sends price-drop emails via Gmail SMTP. Choose <b>Auto</b>, <b>Ask</b> (Y/N each time) or <b>Never</b> mode, and set up or change credentials from the in-app <code>S</code> settings menu.</p>
</td>
<td width="50%" valign="top">
<h4>🎨 Interactive Colored Terminal UI</h4>
<p>A boxed welcome banner, color-coded output via <code>Colorama</code>, robust input validation, and replayable execution loops.</p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h4>🛡️ Seller Authenticity Check</h4>
<p>Best-effort heuristic that labels a listing <b>Official</b>, <b>Third-Party</b> or <b>Unknown</b> from the seller name, and warns on non-HTTPS links. It is a hint, not a guarantee.</p>
</td>
<td width="50%" valign="top">
<h4>🔐 Local Settings File</h4>
<p>Credentials are stored in a git-ignored <code>settings.json</code> created on first run, so nothing sensitive lives in source code.</p>
</td>
</tr>
</table>

<br />

<!-- DEMO SHOWCASE -->
<div id="-live-demo">
<table width="100%">
<tr>
<td align="center" bgcolor="#0d1117">
<h2>🎬 Live Video Demo</h2>
</td>
</tr>
<tr>
<td align="center">
<br />
<a href="https://www.youtube.com/watch?v=M6JfYZhw11Y" target="_blank">
<img src="https://img.youtube.com/vi/M6JfYZhw11Y/maxresdefault.jpg" alt="Amazon BudgetBuy Demo Video" width="92%" style="border-radius: 8px; border: 1px solid #30363d;" />
</a>
<br />
<p><sub><b>▶️ Click the thumbnail above to watch the project demo on YouTube</b></sub></p>
</td>
</tr>
</table>
</div>

<br />

<!-- SAMPLE WORKFLOW EXECUTION -->
<table width="100%">
<tr>
<td align="center" bgcolor="#0d1117">
<h2>🖥️ Sample CLI Workflow</h2>
</td>
</tr>
<tr>
<td>
<pre><code>=================================================================
🛒 BUDGET BUY v2.0 — Multi-Platform Price Tracker
=================================================================

🔗 Paste Product URL (Or 'S' For Settings):
https://www.amazon.in/dp/B0CHX1W1XY

💰 Enter Your Target Price ₹:
50000

⏳ Fetching Product Details Using Amazon Scraper...
🌐 Status Code: 200
-----------------------------------------------------------------
📦 Product:
Apple iPhone 15 (Black, 128 GB)

🧾 Seller        : Appario Retail Private Ltd
🛡️  Authenticity : Likely Official
💰 Current Price: ₹48,999
🎯 Target Price: ₹50,000
-----------------------------------------------------------------

🎉 Product Is Within Your Budget!
📧 Email Alert Sent Successfully!</code></pre>
</td>
</tr>
</table>

<br />

<!-- TECH STACK TABLE -->
<table width="100%">
<tr>
<td align="center" colspan="4" bgcolor="#0d1117">
<h2>🛠️ Core Tech Stack</h2>
</td>
</tr>
<tr align="center">
<td width="25%">
<br />
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="48" alt="Python" /><br /><br />
<b>Python 3.10+</b><br />
<sub>Core Engine</sub>
</td>
<td width="25%">
<br />
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" width="48" alt="BeautifulSoup" /><br /><br />
<b>BeautifulSoup4</b><br />
<sub>DOM Parsing</sub>
</td>
<td width="25%">
<br />
<img src="https://www.vectorlogo.zone/logos/gmail/gmail-icon.svg" width="48" alt="Gmail SMTP" /><br /><br />
<b>smtplib (SMTP)</b><br />
<sub>Email Dispatch</sub>
</td>
<td width="25%">
<br />
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bash/bash-original.svg" width="48" alt="Colorama" /><br /><br />
<b>Colorama</b><br />
<sub>Terminal Styling</sub>
</td>
</tr>
</table>

<br />

<!-- QUICK START & INSTALLATION -->
<div id="-quick-start">
<table width="100%">
<tr>
<td align="center" bgcolor="#0d1117">
<h2>🚀 Quick Start & Installation</h2>
</td>
</tr>
<tr>
<td>
<br />
<ol>
<li><b>Clone the Repository:</b>
<pre><code>git clone https://github.com/guptaji0358/Amazon-BudgetBuy.git
cd Amazon-BudgetBuy</code></pre>
</li>
<li><b>Install Dependencies:</b>
<pre><code>pip install requests beautifulsoup4 colorama</code></pre>
</li>
<li><b>Run the App:</b>
<pre><code>python main.py</code></pre>
</li>
<li><b>First-Run Email Setup:</b>
<p>You will be prompted for your Gmail address, Google App Password, receiver email and send mode (Auto / Ask / Never). Values are saved to <code>settings.json</code>. Type <code>S</code> at the URL prompt anytime to change them.</p>
</li>
</ol>
<br />
</td>
</tr>
</table>
</div>

<br />

<!-- GMAIL APP PASSWORD GUIDE -->
<table width="100%">
<tr>
<td align="center" bgcolor="#0d1117">
<h2>🔐 Gmail App Password Setup Guide</h2>
</td>
</tr>
<tr>
<td>
<br />
<p><i>⚠️ <b>Note:</b> Do NOT use your normal Gmail password. Google blocks standard passwords for SMTP authentication. You must generate a 16-digit <b>Google App Password</b>.</i></p>

<ol>
<li><b>Open Google Account Settings:</b> Go to your Google Account security settings.</li>
<li><b>Enable 2-Step Verification:</b> Search for <code>2-Step Verification</code> and turn it ON.</li>
<li><b>Open App Passwords:</b> Search for <code>App Passwords</code> in the search bar.</li>
<li><b>Generate Password:</b> Select <code>App → Mail</code> and <code>Device → Windows Computer</code> (or your OS), then click <b>Generate</b>.</li>
<li><b>Copy Password:</b> Google will provide a 16-character code (e.g., <code>abcd efgh ijkl mnop</code>). Enter it when the app asks for your <b>Gmail App Password</b>.</li>
</ol>
<br />
</td>
</tr>
</table>

<br />

<!-- SECURITY WARNING -->
<table width="100%">
<tr>
<td align="center" bgcolor="#161b22" style="border: 1px solid #d29922;">
<h3 style="color: #d29922;">🔒 Security Alert</h3>
<p><b>Never upload real Gmail credentials or App Passwords to GitHub!</b><br />
Credentials are saved in <code>settings.json</code>, which is listed in <code>.gitignore</code>. Keep it that way and never commit it.</p>
</td>
</tr>
</table>

<br />

<!-- PROJECT STRUCTURE -->
<table width="100%">
<tr>
<td align="center" bgcolor="#0d1117">
<h2>📁 Project Structure</h2>
</td>
</tr>
<tr>
<td>
<pre><code>BudgetBuy/
├── main.py           # Entry point & main loop
├── banner.py         # Welcome banner
├── display.py        # Product details & authenticity output
├── email_alert.py    # Gmail SMTP alerts
├── settings.py       # settings.json load/save & setup menu
├── config.py         # HTTP headers
└── scrapers/
    ├── base.py       # BaseScraper + authenticity heuristic
    ├── amazon.py
    ├── flipkart.py
    ├── myntra.py
    └── generic.py    # Auto-detect fallback</code></pre>
</td>
</tr>
</table>

<br />

<!-- CONCEPTS MASTERED -->
<table width="100%">
<tr>
<td align="center" bgcolor="#0d1117">
<h2>🧠 Software Engineering Concepts Mastered</h2>
</td>
</tr>
<tr>
<td>
<br />
<ul>
<li><b>Web Scraping & DOM Parsing:</b> Extracting dynamic data using CSS selectors and HTML tags.</li>
<li><b>HTTP Request Handling:</b> Sending custom User-Agent headers to prevent anti-scraping blocks.</li>
<li><b>Automated Email Pipeline:</b> SSL/TLS encrypted SMTP email dispatching with <code>smtplib</code>.</li>
<li><b>Data Cleaning & Validation:</b> Parsing string currencies into float primitives for evaluation.</li>
<li><b>Terminal User Experience:</b> Color-coded CLI workflows using <code>Colorama</code>.</li>
<li><b>Modular Architecture:</b> A <code>BaseScraper</code> class with per-platform subclasses and URL-based scraper selection.</li>
<li><b>Persistent Configuration:</b> JSON-backed settings with interactive first-run setup.</li>
</ul>
<br />
</td>
</tr>
</table>

<br />

<!-- OPEN SOURCE & CONTRIBUTIONS -->
<table width="100%">
<tr>
<td align="center" bgcolor="#0d1117">
<h2>🌟 Open Source & Developer Contribution</h2>
</td>
</tr>
<tr>
<td>
<br />
<p>This project is completely open-source for learning and development. Developers are encouraged to fork, enhance, and build upon this core engine!</p>

<h4>💡 Future Roadmap & Contribution Ideas:</h4>
<ul>
<li>✅ <s>Flipkart, Myntra & generic-site support</s> (done in v2.0)</li>
<li>🛒 <b>Dedicated Meesho & Ajio Scrapers</b></li>
<li>⏰ <b>Scheduled / Background Price Monitoring</b></li>
<li>📊 <b>Price History Analytics & Graphical Dashboard</b></li>
<li>💻 <b>GUI Interface (Tkinter / PyQt)</b></li>
</ul>
<br />
</td>
</tr>
</table>

<br />

<!-- AUTHOR SIGNATURE FOOTER -->
<div align="center">

<hr style="border: 1px solid #30363d;" />

<br />

<h2>👨‍💻 Architect & Lead Developer</h2>
<h1><b><a href="https://github.com/guptaji0358" style="color: #58a6ff; text-decoration: none;">Robin Gupta</a></b></h1>
<p><i>Building Intelligent Web Automation Engines & AI Solutions • 100 Days of Code</i></p>

<br />

<p>
<a href="https://github.com/guptaji0358">
<img src="https://img.shields.io/badge/GitHub-@guptaji0358-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Profile" />
</a>
<a href="https://www.youtube.com/watch?v=M6JfYZhw11Y">
<img src="https://img.shields.io/badge/YouTube-Watch_Demo-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube Demo" />
</a>
</p>

<br />

<p>⭐ <b>Enjoyed this project? Leave a star on the repository to support!</b> ⭐</p>

<br />

<!-- BOTTOM GRAPHIC BANNER -->
<a href="https://github.com/guptaji0358/Amazon-BudgetBuy">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer" width="100%" alt="Footer Banner" />
</a>

<p><sub>Made with Python ❤️ by <b>Robin Gupta</b></sub></p>

</div>
