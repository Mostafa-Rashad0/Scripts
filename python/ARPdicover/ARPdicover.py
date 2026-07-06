
from scapy.all import *
import argparse


def build_arp_packet(ip_range):
    broadcast_mac = "ff:ff:ff:ff:ff:ff"
    ether = Ether(dst=broadcast_mac)
    arp = ARP(pdst=ip_range)

    return ether / arp


def scan_network(ip_range, interface, timeout, inter):
    
    packet = build_arp_packet(ip_range)

    answered, unanswered = srp(
        packet,
        iface=interface,
        timeout=timeout,
        inter=inter,
        verbose=False
    )

    hosts = []

    for sent, received in answered:
        ip = received[ARP].psrc
        mac = received[Ether].src
        hosts.append((ip, mac))

    return hosts


def main():
    parser = argparse.ArgumentParser(
        description="Simple ARP Network Scanner"
    )

    parser.add_argument(
        "ip_range",
        help="Target IP or CIDR range (e.g. 192.168.1.0/24)"
    )

    parser.add_argument(
        "-i",
        "--interface",
        default="eth0",
        help="Network interface (default: eth0)"
    )

    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=2,
        help="Response timeout in seconds (default: 2)"
    )

    parser.add_argument(
        "--inter",
        type=float,
        default=0.1,
        help="Delay between packets in seconds (default: 0.1)"
    )

    args = parser.parse_args()

    print(f"[*] Scanning {args.ip_range}")
    print(f"[*] Interface : {args.interface}")
    print(f"[*] Timeout   : {args.timeout}s")
    print(f"[*] Packet Gap: {args.inter}s\n")

    hosts = scan_network(
        ip_range=args.ip_range,
        interface=args.interface,
        timeout=args.timeout,
        inter=args.inter,
    )

    if hosts:
        print(f"Found {len(hosts)} live host(s)\n")
        print(f"{'IP Address':<20}{'MAC Address'}")
        print("-" * 40)

        for ip, mac in hosts:
            print(f"{ip:<20}{mac}")

    else:
        print("No hosts found.")


if __name__ == "__main__":
    main()
