# -*- coding: utf-8 -*-
# OSINT-Probe v1.0
# Diciptakan oleh Jarvis untuk Tuan Indrakenzo

import socket
import whois
import requests
from termcolor import colored
import sys
import os

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """
     ██████╗ ███████╗██╗███╗   ██╗████████╗   ██████╗  ██████╗  ██████╗ ███████╗
    ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝   ██╔══██╗██╔═══██╗██╔═══██╗██╔════╝
    ██║   ██║███████╗██║██╔██╗ ██║   ██║      ██████╔╝██║   ██║██║   ██║███████╗
    ██║   ██║╚════██║██║██║╚██╗██║   ██║      ██╔══██╗██║   ██║██║   ██║╚════██║
    ╚██████╔╝███████║██║██║ ╚████║   ██║      ██║  ██║╚██████╔╝╚██████╔╝███████║
     ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝      ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝
                            OSINT Probe by Indra-Jarvis
    """
    print(colored(banner, "yellow"))

def get_ip_address(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(colored(f"\n[+] Alamat IP ditemukan:", "green"))
        print(f"    -> {ip}")
    except socket.gaierror:
        print(colored("\n[!] Gagal menemukan alamat IP. Domain tidak valid.", "red"))

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        print(colored(f"\n[+] Informasi WHOIS:", "green"))
        print(f"    -> Registrar: {w.registrar}")
        print(f"    -> Tanggal Dibuat: {w.creation_date}")
        print(f"    -> Tanggal Kedaluwarsa: {w.expiration_date}")
        if w.name_servers:
            print(f"    -> Name Servers:")
            for ns in w.name_servers:
                print(f"        - {ns}")
    except Exception:
        print(colored("\n[!] Gagal mengambil informasi WHOIS.", "red"))

def get_http_headers(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        print(colored(f"\n[+] HTTP Headers:", "green"))
        for header, value in response.headers.items():
            print(f"    -> {header}: {value}")
    except requests.RequestException:
        print(colored(f"\n[!] Gagal mengambil HTTP Headers.", "red"))

if __name__ == "__main__":
    bersihkan_layar()
    print_banner()
    if len(sys.argv) != 2:
        print(colored("\nPenggunaan: python3 probe.py <domain.com>", "cyan"))
        sys.exit(1)
    
    target = sys.argv[1]
    print(colored(f"\n[*] Memulai pengintaian untuk target: {target}", "yellow"))
    print("="*60)
    
    get_ip_address(target)
    get_whois_info(target)
    get_http_headers(target)

    print("\n" + "="*60)
    print(colored("[*] Pengintaian Selesai.", "yellow"))
