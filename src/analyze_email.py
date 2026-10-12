
import sys
from email import policy
from email.parser import BytesParser
from pathlib import Path
from urllib.parse import urlparse


def analyze_email(file_path: str) -> None:
    path = Path(file_path)

    if not path.is_file():
        print(f"Error: File not found: {path}")
        return

    with path.open("rb") as file:
        message = BytesParser(policy=policy.default).parse(file)

    sender = message.get("From", "Not provided")
    reply_to = message.get("Reply-To", "Not provided")
    subject = message.get("Subject", "No subject")
    return_path = message.get("Return-Path", "Not provided")
    authentication = message.get_all("Authentication-Results", [])

    print("=== Email Analysis ===")
    print(f"Subject: {subject}")
    print(f"From: {sender}")
    print(f"Reply-To: {reply_to}")
    print(f"Return-Path: {return_path}")

    print("\n=== Authentication Results ===")

    if authentication:
        for result in authentication:
            print(result)
    else:
        print("No Authentication-Results header found.")

    print("\n=== URLs ===")

    urls_found = False

    for part in message.walk():
        if part.get_content_type() == "text/plain":
            try:
                body = part.get_content()
            except (UnicodeDecodeError, LookupError):
                continue

            for word in body.split():
                candidate = word.strip(".,;!?)\"'<>[")
                if candidate.startswith(("http://", "https://")):
                    parsed = urlparse(candidate)

                    if parsed.hostname:
                        urls_found = True
                        print(f"URL: {candidate}")
                        print(f"Hostname: {parsed.hostname}")

    if not urls_found:
        print("No URLs found in plain-text content.")

    print("\nNote: This program extracts data only.")
    print("It does not independently verify authentication or")
    print("determine whether the email is malicious.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/analyze_email.py <email.eml>")
        sys.exit(1)

    analyze_email(sys.argv[1])