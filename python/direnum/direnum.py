
import requests
import sys


def load_wordlist(filepath):
    try:
        with open(filepath, "r") as f:
            words = [line.strip() for line in f if line.strip()]
        print(f"[*] Loaded {len(words)} entries from {filepath}")
        return words
    except FileNotFoundError:
        print(f"[!] Error: '{filepath}' not found.")
        return []


def enumerate_directories(target_url, wordlist, extension=".html"):
    found = []
    headers = {
            "User-Agent": "Mozilla/5.0"
            }

    for entry in wordlist:
        url = f"{target_url}/{entry}{extension}"
        try:
            r = requests.get(url, headers=headers, timeout=3)
            if r.status_code != 404:
                print(f"[+] {r.status_code} - {url}")
                found.append(url)
        except requests.RequestException:
            pass

    return found


def main():
    if len(sys.argv) < 3:
        print(f"Usage: python3 {sys.argv[0]} <target_url> <wordlist> [extension]")
        print(f"Example: python3 {sys.argv[0]} http://10.10.10.5 wordlist.txt .html")
        sys.exit(1)

    target_url = sys.argv[1]
    wordlist_path = sys.argv[2]
    extension = sys.argv[3] if len(sys.argv)>3 else ".html"

    print(f"[*] Starting directory enumeration for {target_url}")
    wordlist = load_wordlist(wordlist_path)

    if not wordlist:
        print("[!] No words to test. Exiting.")
        sys.exit(1)

    results = enumerate_directories(target_url, wordlist, extension)
    print(f"\n[*] Enumeration complete. Found {len(results)} valid path(s).")


main()
