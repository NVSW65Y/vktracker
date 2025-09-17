from bs4 import BeautifulSoup
import requests
import re

# наверное можно упростить но мне так захотелось и ночью переделывать лень мб потом
def statextract(status):
    # получаем текст но там активность и дата вмести :< а я перфекционист!
    unwrapd = status.get_text(strip=True)
    # делим текст на слова/токены что то
    unsplit = unwrapd.split()
    # не пугаемся, (?<=\D) <- эта штука проверяет чтобы идти вперед если не числа а символы, эта штука проверяет если дата то влево ->  (?=\d{4}-\d{2}-\d{2}) таким образом мы в серединке, второе это пробел -> ' ', и третье это то что мы меняем.
    unsplit[2] = re.sub(r'(?<=\D)(?=\d{4}-\d{2}-\d{2})', ' ', unsplit[2])
    text = " ".join(unsplit) # возращает все обратно в текст
    return text


def GETFHERE():
    vk_id = "id000000001" # VK ID HERE

    url = "https://onli-vk.ru/" + vk_id
    print(f"Requesting URL: {url}")

    try:
        resp = requests.get(url, timeout=5)
        # This will raise an HTTPError for bad responses (ctrl c ctrl v тк лень) 
        resp.raise_for_status()
        # delaet html parsed soup for different soupy actions
        soup = BeautifulSoup(resp.text, 'html.parser')
        # beret raw status from html code
        status = soup.find(id="profile_online")
        if status:
            status = statextract(status)
            print(status)
        else:
            print("no status womp womp")

            #ctrl c ctrl v
    except requests.exceptions.RequestException as e:
        print(f"An error occurred with the network request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    GETFHERE()
