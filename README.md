## Automated CSGO Cheater Reporting Script
This repository contains a Python script designed to automate the process of reporting cheaters in Counter-Strike: Global Offensive (CSGO) matches to the Steam community. The script uses the requests library to interact with the Steam community's abuse reporting API and colorama to enhance terminal output with colored text.

## Features
- Automated Reporting: Efficiently report multiple cheaters in a CSGO match with a single run.
- Clear Terminal Output: Utilizes the colorama library to display colored status messages.
- User Prompts: Prompts for report reason, match ID, and cheater IDs to customize each report.
- Batch Processing: Handles multiple cheater IDs at once, iterating through and submitting individual reports.
= Cross-Platform Compatibility: Clears the terminal screen for both Windows and Unix-based systems.

## Clone Repository:
```bash
git clone https://github.com/yourusername/csgo-cheater-reporting-script.git
cd csgo-cheater-reporting-script
```
## Install Dependencies:
```bash
pip install -r requirements.txt
```
## Usage:
```bash
python report_bot.py
```
## Example Output:
```bash
REASON REPORT: Cheating in match
CSGO MATCH ID: ABC123
GIMME THE CHEATER IDs (comma separated): 12345, 67890

CHEATER ID: 12345 - REPORT SUCCESS
CHEATER ID: 67890 - REPORT SUCCESS
```
![image](https://github.com/ThatNotEasy/ReportBot-CSGO/assets/25004320/031aefda-8332-4f79-8b91-cc7fe3fe53b6)
