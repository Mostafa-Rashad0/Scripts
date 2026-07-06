# ARP Network Scanner

A simple Python-based ARP scanner built with **Scapy** to discover live hosts on a local network. The scanner sends ARP broadcast requests and collects responses to identify active devices and their MAC addresses.

> **Note:** This scanner works only on **local Layer 2 networks**. It does **not** work through Layer 3 VPN interfaces such as OpenVPN `tun` interfaces.

---

## Features

* Discover live hosts on a local network
* Display IP and MAC addresses of responding devices
* Support for single IPs and CIDR ranges
* Configurable network interface
* Configurable timeout
* Configurable delay between packets
* Clean, formatted terminal output
* Built with Scapy

---

## Requirements

* Python 3.8+
* Linux (recommended)
* Root privileges
* Scapy

Install Scapy:

```bash
pip install scapy
```

---

## Usage

```bash
sudo python3 ARPdicover.py <ip_range> [options]
```

### Positional Arguments

| Argument   | Description                                             |
| ---------- | ------------------------------------------------------- |
| `ip_range` | Target IP address or CIDR range (e.g. `192.168.1.0/24`) |

### Optional Arguments

| Flag                | Description                     | Default |
| ------------------- | ------------------------------- | ------- |
| `-i`, `--interface` | Network interface               | `eth0`  |
| `-t`, `--timeout`   | Response timeout (seconds)      | `2`     |
| `--inter`           | Delay between packets (seconds) | `0.1`   |

---

## Examples

Scan an entire subnet:

```bash
sudo python3 ARPdicover.py 192.168.1.0/24
```

Specify a network interface:

```bash
sudo python3 ARPdicover.py 192.168.1.0/24 -i enp7s0
```

Increase timeout:

```bash
sudo python3 ARPdicover.py 192.168.1.0/24 -t 5
```

Specify all options:

```bash
sudo python3 ARPdicover.py 192.168.1.0/24 -i enp7s0 -t 5 --inter 0.2
```

---

## Example Output

```text
[*] Scanning 192.168.1.0/24
[*] Interface : enp7s0
[*] Timeout   : 2s
[*] Packet Gap: 0.1s

Found 4 live host(s)

IP Address          MAC Address
----------------------------------------
192.168.1.1         c4:27:28:42:1f:9c
192.168.1.2         bc:89:f8:eb:bc:6e
192.168.1.4         36:9e:c9:de:2f:f6
192.168.1.8         96:4b:45:19:b4:e6
```

---

## How It Works

1. Builds an Ethernet frame with the broadcast MAC address (`ff:ff:ff:ff:ff:ff`).
2. Creates an ARP request for the specified IP or subnet.
3. Sends the packet using Scapy's `srp()` function.
4. Waits for ARP replies.
5. Extracts each responding host's IP and MAC address.
6. Displays the results in a formatted table.

---

## Limitations

* Works only on the local broadcast domain.
* Requires root privileges to send raw packets.
* Does not discover hosts through routers.
* Does not work over Layer 3 VPN interfaces (`tun0`).
* Some devices may not respond because of sleep mode, client isolation, or firewall settings.

---

## Future Improvements

* Hostname resolution
* MAC vendor lookup
* Export results to CSV/JSON
* Retry mechanism for improved discovery
* Colored terminal output
* Multi-threaded scanning
* Progress indicator

---

## Disclaimer

This project is intended for educational purposes and authorized network administration only. Only scan networks that you own or have explicit permission to test.

---
