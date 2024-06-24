from googlesearch import search
from fake_useragent import UserAgent

def dork_google(dork_query, num_results=10):
    try:
        ua = UserAgent()
        user_agent = ua.random
        print(f"Using User-Agent: {user_agent}")

        results = search(dork_query, num_results=num_results, user_agent=user_agent)

        if results:
            print("Search results:")
            for idx, link in enumerate(results, start=1):
                print(f"{idx}. {link}")
            return results
        else:
            print("No results found for the dork.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_results_to_file(results, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for link in results:
                file.write(f"{link}\n")
        print(f"Results saved to {filename}")
    except Exception as e:
        print(f"Failed to save results: {e}")

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
    num_results = int(input("Berapa hasil yang ingin ditampilkan? (Default: 10): ") or 10)
    want_save = input("Ingin disave? (y/n): ").lower()

    if want_save == 'y':
        filename = input("Nama file untuk menyimpan hasil: ")
        results = dork_google(dork_query, num_results)
        if results:
            save_results_to_file(results, f"{filename}.txt")
    elif want_save == 'n':
        dork_google(dork_query, num_results)
    else:
        print("Pilihan tidak valid. Harap masukkan 'y' atau 'n'.")

if __name__ == "__main__":
    main()
