# Brutepy
Bruteforce Script
This is a simple bruteforce script that tries to log in to a website using a list of words as both the username and password. The script uses the requests library to send HTTP requests to the server and checks the response status code to determine if the login was successful.

Usage
To use the script, simply run it with the URL you want to bruteforce as the first argument:

bash
Edit
Full Screen
Copy code
python bruteforce.py <URL>
The script will prompt you to choose between using a dictionary or generating random words for the bruteforce attack. If you choose to use a dictionary, you will be prompted to enter the path to the dictionary file. If you choose to generate random words, you will be prompted to enter the length of the words and the number of words to generate.

The script will then attempt to log in to the website using each word in the list. If the login is successful, the script will print the word and exit. If the login fails, the script will move on to the next word. If a network error occurs, the script will prompt you to try again or enter a new URL.

Requirements
The script requires the following Python libraries:

requests
You can install the requests library using pip:

Edit
Full Screen
Copy code
pip install requests
Limitations
The script has a few limitations:

It assumes that the website uses a form with the names username and password.
It does not handle CAPTCHAs or other anti-bot measures.
It does not use a thread pool or other concurrency mechanism, so it may be slow for large lists of words.
Disclaimer
This script is intended for educational purposes only and should not be used for malicious purposes. Unauthorized access to a computer system or network is illegal and punishable by law. The author of this script is not responsible for any misuse of this code.
