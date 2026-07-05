import requests
import sys

def load_wordlist(filepath):
    try:
        with open(filepath, "r") as f:
            words=[line.strip() for line in f if line.strip()] #For every line in the file, if it isn't empty after stripping whitespace, put the stripped version into a list.
        print(f"[*] Loaded {len(words)} entries from {filepath}")
        return words
    except FileNotFoundError:
        print(f"[!] Error: '{filepath}' not found.")
        return []


def enumerate_subdomains(domain, wordlist):
    found = []
    headers = {
            "User-Agent": "Mozilla/5.0"
            }
    for sub in wordlist:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, headers=headers, timeout=4)
            print(f"[+] {url} ({response.status_code})")
            found.append(url)
        except requests.RequestException:
            pass
    return found




def main():
    if len(sys.argv) != 3 :
        print(f"Usage: python3 {sys.argv[0]} <domain> <wordlist>")
        sys.exit(1)
    domain = sys.argv[1]
    wordlist_path = sys.argv[2]

    print(f"[*] Starting subdomain enumeration for {domain}")
    wordlist = load_wordlist(wordlist_path)

    if not wordlist:
        print("[!] No words to test. Exiting.")
        sys.exit(1)

    results = enumerate_subdomains(domain, wordlist)
    print(f"\n[*] Enumeration complete. Found {len(results)} subdomain(s).")









if __name__ == "__main__":
    main()

