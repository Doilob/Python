# httpstat.us/
# |▌▌▌▌ |
# |▌▌▌▌▌|
import time
from requests import get

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            print(results)
            return True
        if reply[0] == 'n':
            return False

results = {}
websites = (
    "httpstat.us/101",  #100series
    "httpstat.us/201",  #200series
    "google.com",
    "instagram.com",
    "naver.com",
    # "nomadcoders.co",
    "youtube.com",
    "httpstat.us/306",  #300series
    "httpstat.us/401",  #400series
    "httpstat.us/501",  #500series  
)
for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
        response = get(website)
        respNum = response.status_code
    if respNum >= 100 and respNum < 200:
        results[website] = "✅"
    if respNum >= 200 and respNum < 300:
        results[website] = "✅"
    if respNum >= 300 and respNum < 400:
        results[website] = "✅"
    if respNum >= 400 and respNum < 500:
        results[website] = "🤔"
    if respNum >= 500 and respNum < 600:
        results[website] = "⛔"

print("|     |", end="")
time.sleep(1)
print("\r|▌    |", end="")
time.sleep(1)
print("\r|▌▌   |", end="")
time.sleep(1)
print("\r|▌▌▌  |", end="")
time.sleep(1)
print("\r|▌▌▌▌ |", end="")
time.sleep(1)
print("\r|▌▌▌▌▌|")
time.sleep(1)
print("Done!")
yes_or_no("Do you want see result?")