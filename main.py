# main.py
import argparse
from port_scanner import PortScanner
from brute_forcer import HTTPBruteForcer

def main():
    parser = argparse.ArgumentParser(description="Python Penetration Testing Toolkit")
    subparsers = parser.add_subparsers(dest="module", required=True)

    # Port Scanner args
    ps_parser = subparsers.add_parser("portscan", help="Port scanning module")
    ps_parser.add_argument("target", help="Target IP or domain")
    ps_parser.add_argument("--ports", help="Comma separated ports (e.g., 22,80,443)")

    # Brute Forcer args
    bf_parser = subparsers.add_parser("bruteforce", help="HTTP Basic Auth brute force")
    bf_parser.add_argument("url", help="URL protected by Basic Auth")
    bf_parser.add_argument("username", help="Username to brute force")
    bf_parser.add_argument("password_file", help="File with passwords to try")

    args = parser.parse_args()

    if args.module == "portscan":
        ports = None
        if args.ports:
            ports = list(map(int, args.ports.split(",")))
        scanner = PortScanner(args.target, ports)
        scanner.run()

    elif args.module == "bruteforce":
        with open(args.password_file, "r") as f:
            passwords = [line.strip() for line in f]
        bf = HTTPBruteForcer(args.url, args.username, passwords)
        bf.run()

if __name__ == "__main__":
    main()
