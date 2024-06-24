import requests
from bs4 import BeautifulSoup
from googlesearch import search
from fake_useragent import UserAgent

def dork_google(dork_query, num_results):
    user_agent = UserAgent().random
    headers = {
        'User-Agent': user_agent
    }
    try:
        results = search(dork_query, stop=num_results, user_agent=user_agent)
        results_list = []
        for result in results:
            print(f"Link: {result}\n")
            results_list.append(result)
        return results_list
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def save_results_to_file(results, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(f"{result}\n")
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
    num_results = int(input("Berapa? : "))
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
    
