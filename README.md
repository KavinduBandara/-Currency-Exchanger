🔴 Currency Exchanger CLI 🔴
A simple Python command-line tool that converts currencies in real-time using the Frankfurter API.

✅ Features
Convert any base currency to a target currency.

Real-time exchange rates from Frankfurter API.

Input validation for:

Base currency

Target currency

Amount

Option to repeat conversions without restarting the program.

🛠 Requirements
Python 3.x

requests library

Install the dependency:

bash
Copy
Edit
pip install requests
▶ How to Run
bash
Copy
Edit
python main.py
💻 Example Output
vbnet
Copy
Edit
🔴WELCOME TO CURRENCY EXCHANGER🔴

Base Currency:💲 USD
Target Currency:💲 LKR

What's the base amount? 100

💱 100 USD is 32,500.0 LKR
Do you wanna try another time?(yes/no): yes
🔮 Future Improvements
Validate base currency from JSON (not just HTTP status).

Add multiple currency conversion in one go.

🙏 Credits
This project was fully coded and structured by me, including:

Handling user input loops

Validating currencies

Adding a repeat feature for multiple conversions

I used ChatGPT by OpenAI for conceptual guidance and help with the README. All coding decisions and final implementation were my own.
