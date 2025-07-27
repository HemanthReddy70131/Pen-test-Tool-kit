# port_scanner.py
import socket

class PortScanner:
    def __init__(self, target, ports=None):
        self.target = target
        self.ports = ports if ports else range(1, 1025)
        self.open_ports = []

    def scan_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            sock.close()
            return result == 0
        except Exception:
            return False

    def run(self):
        print(f"Scanning {self.target} for open ports...")
        for port in self.ports:
            if self.scan_port(port):
                print(f"[+] Port {port} is open")
                self.open_ports.append(port)
        if not self.open_ports:
            print("No open ports found.")
        return self.open_ports
