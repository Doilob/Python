import time
from requests import get

websites = (
    "https://google.com",
    "https://youtube.com",
    "https://naver.com",
    "https://instagram.com"
    )

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            print(results)
            return True
        if reply[0] == 'n':
            return False
results = {

}
for website in websites:
    if not website.startswith("https://"):
        print(website + " This website is have to fix!")
        website = f"https://{website}"
        response = get(website)
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print("..")
        time.sleep(0.5)
        print("...")
    response = get(website)
    if response.status_code == 200:
        results[website] = "OK"
        time.sleep(0.75)
    else:
        results[website] = "FAILED"
        time.sleep(0.75)
print("Done!")
yes_or_no("Do you want see results?")