from bs4 import BeautifulSoup
from utilities.mail import send_mail
import numpy as np
import requests
import json
import os

# List of CSS colors to choose from for the background color of the email
colors = ['Tomato', 'Gold', 'Teal', 'LightCoral', 'DodgerBlue', 'SpringGreen', 'LightGreen',
          'Plum', 'PeachPuff', 'LightSlateGray', 'SandyBrown', 'Orange', 'Snow', 'HoneyDew',
          'MintCream', 'Azure', 'AliceBlue', 'GhostWhite', 'WhiteSmoke', 'SeaShell', 'Beige', 'OldLace',
          'FloralWhite', 'Ivory', 'AntiqueWhite', 'Linen', 'LavenderBlush', 'MistyRose']

diff_colors = ['Snow', 'HoneyDew', 'MintCream', 'Azure', 'AliceBlue', 'GhostWhite', 'WhiteSmoke', 'SeaShell', 'Beige',
               'OldLace', 'FloralWhite', 'Ivory']

# Selecting random color from colors
color = colors[np.random.randint(0, len(colors) - 1)]

if color in diff_colors:
    font_color = "lightgrey"
else:
    font_color = "white"

# Getting word of the day from Merriam Webster website
url = 'https://www.merriam-webster.com/word-of-the-day'
s = requests.Session()

# Headers for User Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

r = s.get(url, headers=headers)

# Checking for Errors
r.raise_for_status()

# Parsing returned data
soup = BeautifulSoup(r.text, 'lxml')

# Getting the word of the day
wotd = soup.find(class_='word-and-pronunciation').text.strip().splitlines()[0].capitalize()

# Getting parts of speech (example: adjective)
attributes = soup.find(class_='main-attr').text

# Getting the pronunciation
syllables = soup.find(class_='word-syllables').text

# Selecting the <div> with list of definitions (there can be more than 1 and be a numbered list)
def_wrapper = soup.select('div .wod-definition-container > p')

defs = ''

# Extracting the definitions
for meaning in def_wrapper:
    defs += meaning.text.strip() + '<div>&nbsp;</div>'

# Getting the 'Did You Know' section
dyk = soup.select_one('div .left-content-box > p').text.strip()

# Preparing the email through SendGrid
email_from = os.getenv('EMAIL_FROM')
email_to = json.loads(os.getenv('EMAIL_TO'))
email_name = os.getenv('EMAIL_NAME')
email_sub = os.getenv('EMAIL_SUBJECT')
email_msg = """
<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link href="https://fonts.googleapis.com/css?family=M+PLUS+Rounded+1c:700&display=swap" rel="stylesheet">

    <style type="text/css">
        body, table, div {
            font-family: 'M PLUS Rounded 1c', sans-serif !important;
            color: """ + font_color + """ !important;
            background-color: """ + color + """;
        }

        table.wrapper {
            width: 100% !important;
            table-layout: fixed;
        }
        
        @media screen and (max-width: 600px) {
            table, div {
            width: 100%;
            }
            body, table, div {
            color: """ + font_color + """ !important;
            }
        }
    </style>
</head>

<body>
    <div>
        <table cellpadding="10" cellspacing="10" border="0" width="100%" class="wrapper">
            <tr>
                <td>
                    <div style="font-size: 50px;">""" + wotd + """</div>&nbsp;
                    <div style="font-size: 25px;">""" + attributes + " | " + syllables + """</div>&nbsp;&nbsp;&nbsp;
                    <div style="font-size: 22px;">Definition(s):</div>&nbsp;
                    <div style="font-size: 20px;">""" + defs + """</div>&nbsp;&nbsp;
                    <div style="font-size: 22px;">Did You Know?</div>&nbsp;&nbsp;
                    <div style="font-size: 20px;">""" + dyk + """</div>
                </td>
            </tr>
        </table>
    </div>
</body>

</html>
"""

if __name__ == '__main__':
    send_mail(email_from, email_to, email_name, email_sub, email_msg)
