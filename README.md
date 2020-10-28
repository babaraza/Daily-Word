[![Python 3.7](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/downloads/release/python-374/)

# Daily Word

Script that emails the **word of the day** from `www.merriam-webster.com`



#### Features

* Get the word of the day
* Includes pronunciation 
* Also, gets the **Did You Know?** section
* Different color background everyday



#### Usage

- Script can be deployed on a Raspberry Pi 
  - User can setup `cronjob` to run every day 
    - User will get a new word every day
  - Uses `SendGrid` to send the emails
  - Can use `.env` or system defined environment variables



##### The script requires the following environment variables

| Environment Variable Name | Example             | Notes                                                 |
| ------------------------- | ------------------- | ----------------------------------------------------- |
| EMAIL_FROM                | example@example.com | The email sender for the word of the day email        |
| EMAIL_TO                  | example@example.com | The email that will receive the word of the day email |
| EMAIL_NAME                | Daily Word          | Name that will appear as senders name in your inbox   |
| EMAIL_SUBJECT             | Word of the Day     | Subject for the email                                 |

