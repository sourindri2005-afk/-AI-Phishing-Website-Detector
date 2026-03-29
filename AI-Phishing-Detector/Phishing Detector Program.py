print("Phishing Detector Program")
print("Enter 'exit' to stop\n")

while True:
    url = input("Enter website URL: ")

    if url.lower() == "exit":
        print("Program ended")
        break

    if url == "":
        print("Please enter something\n")
        continue

    risk = 0

    if not url.startswith("https://"):
        print("Site is not secure")
        risk += 1

    if len(url) > 70:
        print("URL seems too long")
        risk += 1

    if "@" in url:
        print("Suspicious '@' found")
        risk += 1

    if "-" in url:
        print("Dash '-' detected")
        risk += 1

    if "." not in url:
        print("Invalid URL format")
        risk += 1

    words = ["login", "verify", "bank"]
    for w in words:
        if w in url.lower():
            print("Suspicious word:", w)
            risk += 1

    if risk >= 3:
        print("This site looks unsafe\n")
    else:
        print("This site looks safe\n")