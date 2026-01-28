#!/usr/bin/env python3
# IP Tracker Script by AN0M949 - FIXED VERSION

import requests
import json
import sys
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def banner():
    # FIX: Use Python 'or' instead of bash '||'
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(Fore.RED + '''
________  _______    ______    ______   __    __        __           
/        |/       \  /      \  /      \ /  |  /  |      /  |          
$$$$$$$$/ $$$$$$$  |/$$$$$$  |/$$$$$$  |$$ | /$$/       $$/   ______  
   $$ |   $$ |__$$ |$$ |__$$ |$$ |  $$/ $$ |/$$/        /  | /      \ 
   $$ |   $$    $$< $$    $$ |$$ |      $$  $$<         $$ |/$$$$$$  |
   $$ |   $$$$$$$  |$$$$$$$$ |$$ |   __ $$$$$  \        $$ |$$ |  $$ |
   $$ |   $$ |  $$ |$$ |  $$ |$$ \__/  |$$ |$$  \       $$ |$$ |__$$ |
   $$ |   $$ |  $$ |$$ |  $$ |$$    $$/ $$ | $$  |      $$ |$$    $$/ 
   $$/    $$/   $$/ $$/   $$/  $$$$$$/  $$/   $$/       $$/ $$$$$$$/  
                                                            $$ |      
                                                            $$ |      
                                                            $$/       
    ''')
    print(Fore.CYAN + "IP Tracker v1.0 | AN0M949 Tools")
    print(Fore.YELLOW + "=" * 50)

def track_ip(ip_address=None):
    if not ip_address:
        # Get own IP if none provided
        try:
            response = requests.get('https://api.ipify.org?format=json', timeout=5)
            ip_address = response.json()['ip']
            print(Fore.GREEN + f"[+] Tracking your IP: {ip_address}")
        except Exception as e:
            print(Fore.RED + f"[-] Cannot get IP address: {e}")
            return
    
    # Multiple API endpoints
    apis = [
        {"url": f"http://ip-api.com/json/{ip_address}", "type": "ip-api"},
        {"url": f"https://ipinfo.io/{ip_address}/json", "type": "ipinfo"},
        {"url": f"http://ipwho.is/{ip_address}", "type": "ipwhois"}
    ]
    
    for api in apis:
        try:
            print(Fore.CYAN + f"\n[+] Querying: {api['type']}")
            response = requests.get(api['url'], timeout=10)
            data = response.json()
            
            if api['type'] == "ip-api":
                if data.get('status') == 'success':
                    display_ip_api(data, ip_address)
                    break
                    
            elif api['type'] == "ipinfo":
                if 'ip' in data:
                    display_ipinfo(data, ip_address)
                    break
                    
            elif api['type'] == "ipwhois":
                if 'success' in data and data['success']:
                    display_ipwhois(data, ip_address)
                    break
                    
        except Exception as e:
            print(Fore.RED + f"[-] API {api['type']} failed: {e}")
            continue
    
    print(Fore.YELLOW + "\n" + "=" * 50)

def display_ip_api(data, original_ip):
    print(Fore.GREEN + "\n[+] IP TRACKING SUCCESS!")
    print(Fore.YELLOW + "=" * 50)
    print(Fore.CYAN + f"IP Address    : {data.get('query', original_ip)}")
    print(Fore.CYAN + f"Country       : {data.get('country', 'N/A')}")
    print(Fore.CYAN + f"Region        : {data.get('regionName', 'N/A')}")
    print(Fore.CYAN + f"City          : {data.get('city', 'N/A')}")
    print(Fore.CYAN + f"ZIP Code      : {data.get('zip', 'N/A')}")
    print(Fore.CYAN + f"Latitude      : {data.get('lat', 'N/A')}")
    print(Fore.CYAN + f"Longitude     : {data.get('lon', 'N/A')}")
    print(Fore.CYAN + f"ISP           : {data.get('isp', 'N/A')}")
    print(Fore.CYAN + f"Organization  : {data.get('org', 'N/A')}")
    print(Fore.CYAN + f"Timezone      : {data.get('timezone', 'N/A')}")
    
    if data.get('lat') and data.get('lon'):
        print(Fore.YELLOW + f"\n[+] Google Maps: https://maps.google.com/?q={data['lat']},{data['lon']}")

def display_ipinfo(data, original_ip):
    print(Fore.GREEN + "\n[+] IP TRACKING SUCCESS!")
    print(Fore.YELLOW + "=" * 50)
    print(Fore.CYAN + f"IP Address    : {data.get('ip', original_ip)}")
    print(Fore.CYAN + f"Hostname      : {data.get('hostname', 'N/A')}")
    print(Fore.CYAN + f"City          : {data.get('city', 'N/A')}")
    print(Fore.CYAN + f"Region        : {data.get('region', 'N/A')}")
    print(Fore.CYAN + f"Country       : {data.get('country', 'N/A')}")
    print(Fore.CYAN + f"Location      : {data.get('loc', 'N/A')}")
    print(Fore.CYAN + f"Organization  : {data.get('org', 'N/A')}")
    print(Fore.CYAN + f"Postal        : {data.get('postal', 'N/A')}")
    print(Fore.CYAN + f"Timezone      : {data.get('timezone', 'N/A')}")
    
    if 'loc' in data and data['loc'] != 'N/A':
        lat, lon = data['loc'].split(',')
        print(Fore.YELLOW + f"\n[+] Google Maps: https://maps.google.com/?q={lat},{lon}")

def display_ipwhois(data, original_ip):
    print(Fore.GREEN + "\n[+] IP TRACKING SUCCESS!")
    print(Fore.YELLOW + "=" * 50)
    print(Fore.CYAN + f"IP Address    : {data.get('ip', original_ip)}")
    print(Fore.CYAN + f"Type          : {data.get('type', 'N/A')}")
    print(Fore.CYAN + f"Continent     : {data.get('continent', 'N/A')}")
    print(Fore.CYAN + f"Country       : {data.get('country', 'N/A')}")
    print(Fore.CYAN + f"Region        : {data.get('region', 'N/A')}")
    print(Fore.CYAN + f"City          : {data.get('city', 'N/A')}")
    print(Fore.CYAN + f"Latitude      : {data.get('latitude', 'N/A')}")
    print(Fore.CYAN + f"Longitude     : {data.get('longitude', 'N/A')}")
    print(Fore.CYAN + f"ISP           : {data.get('connection', {}).get('isp', 'N/A')}")
    print(Fore.CYAN + f"Organization  : {data.get('connection', {}).get('org', 'N/A')}")
    print(Fore.CYAN + f"Timezone      : {data.get('timezone', {}).get('id', 'N/A')}")
    
    if data.get('latitude') and data.get('longitude'):
        print(Fore.YELLOW + f"\n[+] Google Maps: https://maps.google.com/?q={data['latitude']},{data['longitude']}")

def bulk_track():
    try:
        with open('ips.txt', 'r') as f:
            ips = [line.strip() for line in f if line.strip()]
        
        if not ips:
            print(Fore.RED + "[-] No IPs found in ips.txt")
            return
            
        print(Fore.GREEN + f"[+] Tracking {len(ips)} IPs from ips.txt")
        
        results = []
        for ip in ips:
            print(Fore.YELLOW + f"\n{'='*30}")
            print(Fore.CYAN + f"[+] Tracking: {ip}")
            
            # Simple API call for bulk
            try:
                response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
                data = response.json()
                
                if data.get('status') == 'success':
                    print(Fore.GREEN + f"    Country: {data.get('country')}")
                    print(Fore.GREEN + f"    ISP: {data.get('isp')}")
                    results.append({
                        'ip': ip,
                        'country': data.get('country'),
                        'isp': data.get('isp'),
                        'city': data.get('city')
                    })
                else:
                    print(Fore.RED + f"    Failed: {data.get('message', 'Unknown error')}")
                    
            except Exception as e:
                print(Fore.RED + f"    Error: {e}")
        
        # Save results
        if results:
            with open('results.txt', 'w') as f:
                for r in results:
                    f.write(f"{r['ip']} | {r['country']} | {r['city']} | {r['isp']}\n")
            print(Fore.GREEN + f"\n[+] Results saved to results.txt")
            
    except FileNotFoundError:
        print(Fore.RED + "[-] File ips.txt not found!")
        print(Fore.YELLOW + "[+] Create ips.txt with one IP per line")

if __name__ == "__main__":
    banner()
    
    print(Fore.CYAN + "\n[1] Track your own IP")
    print("[2] Track specific IP")
    print("[3] Bulk track from ips.txt")
    print("[4] Exit")
    
    try:
        choice = input(Fore.YELLOW + "\n[+] Select option: ").strip()
        
        if choice == "1":
            track_ip()
        elif choice == "2":
            ip = input(Fore.YELLOW + "[+] Enter IP address: ").strip()
            if ip:
                track_ip(ip)
            else:
                print(Fore.RED + "[-] No IP provided")
        elif choice == "3":
            bulk_track()
        elif choice == "4":
            print(Fore.RED + "\n[!] Exiting...")
            sys.exit(0)
        else:
            print(Fore.RED + "[-] Invalid choice")
            
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[!] Interrupted by user")
        sys.exit(0)
    
    input(Fore.YELLOW + "\n[+] Press Enter to exit...")