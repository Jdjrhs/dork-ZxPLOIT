import requests
from bs4 import BeautifulSoup

def dork_google(dork_query, num_results):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    url = f"https://www.google.com/search?q={dork_query}&num={num_results}"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('div', class_='tF2Cxc')
            if not results:
                print("Sorry, the dork returned no results.")
            else:
                for result in results:
                    title = result.find('h3').get_text()
                    link = result.find('a')['href']
                    print(f"Title: {title}")
                    print(f"Link: {link}\n")
            return soup
        else:
            print(f"Failed to fetch results. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def save_results_to_file(results, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for result in results:
            title = result.find('h3').get_text()
            link = result.find('a')['href']
            file.write(f"{link}\n")
    print(f"Results saved to {filename}")

def main():
    print("""
 ___                 _         _______        ___    _      _____  _  _____ 
(  _`\              ( )       (_____  )      (  _`\ ( )    (  _  )(_)(_   _)
| | ) |   _    _ __ | |/')______   /'/'      | |_) )| |    | ( ) || |  | |  
| | | ) /'_`\ ( '__)| , <(______)/'/'  (`\/')| ,__/'| |  _ | | | || |  | |  
| |_) |( (_) )| |   | |\`\     /'/'___  >  < | |    | |_( )| (_) || |  | |  
(____/'`\___/'(_)   (_) (_)   (_______)(_/\_)(_)    (____/'(_____)(_)  (_)  
by ZxPLOIT and ChatGpt
    """)
    dork_query = input("Dork: ")
    num_results = input("Berapa? : ")
    want_save = input("Ingin disave? (y/n): ").lower()
    
    if want_save == 'y':
        filename = input("Nama: ")
        results = dork_google(dork_query, num_results)
        if results:
            save_results_to_file(results, f"{filename}.txt")
    elif want_save == 'n':
        dork_google(dork_query, num_results)
    else:
        print("Pilihan tidak valid. Harap masukkan 'y' atau 'n'.")

if __name__ == "__main__":
    main()
