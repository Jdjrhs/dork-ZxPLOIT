import requests
from bs4 import BeautifulSoup

def dork_google(dork_query, num_results):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    url = f"https://www.google.com/search?q={dork_query}&num={num_results}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('div', class_='tF2Cxc')
        
        if not results:
            print("Sorry, the dork returned no results.")
        else:
            for result in results:
                title_tag = result.find('h3')  # Find the <h3> tag containing the title
                if title_tag:
                    title = title_tag.get_text(strip=True)  # Get the text of the title, stripping any whitespace
                else:
                    title = "Title not found"

                link_tag = result.find('a')  # Find the <a> tag containing the link
                if link_tag and 'href' in link_tag.attrs:
                    link = link_tag['href']  # Get the 'href' attribute of the <a> tag
                else:
                    link = "Link not found"

                print(f"Title: {title}")
                print(f"Link: {link}\n")

        return results

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def save_results_to_file(results, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for result in results:
                link_tag = result.find('a')
                if link_tag and 'href' in link_tag.attrs:
                    link = link_tag['href']
                    file.write(f"{link}\n")
                else:
                    print("Link not found, skipping...")
    except Exception as e:
        print(f"Error saving results to file: {e}")

def main():
    print("""
 ___                 _         _______        ___    _      _____  _  _____ 
(  _`\              ( )       (_____  )      (  _`\ ( )    (  _  )(_)(_   _)
| | ) |   _    _ __ | |/')______   /'/'      | |_) )| |    | ( ) || |  | |  
| | | ) /'_`\ ( '__)| , <(______)/'/'  (`\/')| ,__/'| |  _ | | | || |  | |  
| |_) |( (_) )| |   | |\`\     /'/'___  >  < | |    | |_( )| (_) || |  | |  
(____/'`\___/'(_)   (_) (_)   (_______)(_/\_)(_)    (____/'(_____)(_)  (_)  
By ZxPLOIT and ChatGpt
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
