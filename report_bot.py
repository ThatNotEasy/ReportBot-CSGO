import requests
import json
import os
from colorama import Fore

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def report_bot(REASON_REPORT, CHEATER_IDS, MATCH_ID):
    cheater_ids_list = CHEATER_IDS.split(',')
    for cheater_id in cheater_ids_list:
        cheater_id = cheater_id.strip()
        cookies = {
            'timezoneOffset': '28800,0',
            'browserid': '3158790170469917446',
            'recentlyVisitedAppHubs': '730',
            'strInventoryLastContext': '730_2',
            'steamCountry': 'MY%7Ce85eef003e9e2ec2ed7a53096068af30',
            'steamLoginSecure': '76561199304547601%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEVFQl8yNDg5MzZCNV83Q0EzRCIsICJzdWIiOiAiNzY1NjExOTkzMDQ1NDc2MDEiLCAiYXVkIjogWyAid2ViOmNvbW11bml0eSIgXSwgImV4cCI6IDE3MTgwNDAzOTEsICJuYmYiOiAxNzA5MzEyODA2LCAiaWF0IjogMTcxNzk1MjgwNiwgImp0aSI6ICIwRUUwXzI0ODkzNkREXzE4QjQzIiwgIm9hdCI6IDE3MTc2NTk0MzgsICJydF9leHAiOiAxNzM2MDE1NDg2LCAicGVyIjogMCwgImlwX3N1YmplY3QiOiAiMTEzLjIxMC41MS4xMTAiLCAiaXBfY29uZmlybWVyIjogIjExMy4yMTAuNTEuMTEwIiB9.UG5mhzLEcFnlta1EK-JcdraQ88Gzf-87dufIJWS1SwYdmCsr25rbI4gpQhhaF70dxkunoofV0SlY-W1pDyuWAA',
            'sessionid': 'a55ee8864f945ee7e36d93f1',
            'webTradeEligibility': '%7B%22allowed%22%3A0%2C%22reason%22%3A256%2C%22allowed_at_time%22%3A1718091285%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22expiration%22%3A1717954325%2C%22time_checked%22%3A1717954025%7D',
        }

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,ms;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://steamcommunity.com',
            'Referer': f'https://steamcommunity.com/profiles/{cheater_id}/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'sessionid': 'a55ee8864f945ee7e36d93f1',
            'json': '1',
            'abuseID': cheater_id,
            'eAbuseType': '10',
            'abuseDescription': REASON_REPORT + MATCH_ID,
            'ingameAppID': '730',
        }

        response = requests.post('https://steamcommunity.com/actions/ReportAbuse/', cookies=cookies, headers=headers, data=data)
        if response.status_code == 200:
            print(f"{Fore.YELLOW}CHEATER ID: {Fore.RED}{cheater_id} - {Fore.GREEN}REPORT SUCCESS")
        else:
            print(f"{Fore.YELLOW}CHEATER ID: {Fore.RED}{cheater_id} - {Fore.RED}REPORT FAILED")

if __name__ == "__main__":
    clear_screen()
    print(
        f"""{Fore.MAGENTA}
            ██████╗███████╗ ██████╗  ██████╗       ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗██████╗  ██████╗ ████████╗
            ██╔════╝██╔════╝██╔════╝ ██╔═══██╗      ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗╚══██╔══╝
            ██║     ███████╗██║  ███╗██║   ██║█████╗██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   ██████╔╝██║   ██║   ██║   
            ██║     ╚════██║██║   ██║██║   ██║╚════╝██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══██╗██║   ██║   ██║   
            ╚██████╗███████║╚██████╔╝╚██████╔╝      ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ██████╔╝╚██████╔╝   ██║   
            ╚═════╝╚══════╝ ╚═════╝  ╚═════╝       ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═════╝  ╚═════╝    ╚═╝   
            {Fore.RESET}"""
    )
    REASON_REPORT = input("REASON REPORT: ")
    MATCH_ID = input("CSGO MATCH ID: ")
    CHEATER_IDS = input("GIMME THE CHEATER IDs (comma separated): ")
    while True:
        report_bot(REASON_REPORT, CHEATER_IDS, MATCH_ID)
