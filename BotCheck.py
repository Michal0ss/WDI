import requests
import time
import schedule
from bs4 import BeautifulSoup

# Dane logowania (zmień na własne)
LOGIN_URL = "https://upel.agh.edu.pl/login/index.php"
GRADES_URL = "https://upel.agh.edu.pl/grade/report/user/index.php?id=7181"
USERNAME = "twoj_login"
PASSWORD = "twoje_haslo"

# Zapisz poprzedni wynik, aby wykrywać zmiany
previous_result = None

def login_and_get_grades():
    global previous_result

    with requests.Session() as session:
        # Pobierz stronę logowania, aby uzyskać token
        login_page = session.get(LOGIN_URL)
        soup = BeautifulSoup(login_page.text, "html.parser")
        token_input = soup.find("input", {"name": "logintoken"})
        login_token = token_input["value"] if token_input else None

        # Dane do logowania
        payload = {
            "username": USERNAME,
            "password": PASSWORD,
            "logintoken": login_token
        }

        # Zaloguj się
        response = session.post(LOGIN_URL, data=payload)

        if "Błąd logowania" in response.text:
            print("Nie udało się zalogować. Sprawdź dane logowania.")
            return

        # Pobierz stronę z ocenami
        grades_page = session.get(GRADES_URL)
        soup = BeautifulSoup(grades_page.text, "html.parser")

        # Znajdź wynik drugiego terminu
        result_element = soup.find("td", class_="grade")  # <- Zmień selektor na odpowiedni
        if not result_element:
            print("Nie znaleziono wyników.")
            return

        current_result = result_element.text.strip()

        # Sprawdź, czy wynik się zmienił
        if previous_result is None:
            print(f"Aktualny wynik: {current_result}")
        elif previous_result != current_result:
            print(f"Nowy wynik! {current_result}")
            # Tutaj można dodać np. powiadomienie przez e-mail lub Telegram

        previous_result = current_result

# Ustaw sprawdzanie co 5 minut
schedule.every(5).minutes.do(login_and_get_grades)

print("Bot rozpoczął działanie. Sprawdzanie co 5 minut...")
while True:
    schedule.run_pending()
    time.sleep(1)
