# Fetch news from Times Of India based on location 
import requests
from bs4 import BeautifulSoup
import webbrowser
import time


def fetch_news_times_of_india(topic, headers):
    """
    Fetch news from Times of India based on the given topic.
    """
    base_url = "https://timesofindia.indiatimes.com/india/"
    search_url = f"{base_url}{topic}"

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    news_items = soup.find_all(class_="w_tle")

    if not news_items:
        return []

    news_list = []
    for item in news_items:
        title = item.find("a").get_text()
        link = base_url + item.find("a")["href"]
        news_list.append((title, link))
    
    return news_list


def display_news(news_list):
    """
    Display the list of news and prompt the user to open links.
    """
    bold_start = "\033[1m"
    bold_end = "\033[0m"

    if not news_list:
        print("Sorry, no news available.")
        return

    print("\nNews available: 😊")
    for idx, (title, link) in enumerate(news_list, 1):
        print(f"{bold_start}\033[1;32;40m \nNEWS {idx}:{bold_end} {bold_start}{title}{bold_end}")
        open_link = input("For more details -> (y/n): ").strip().lower()
        if open_link == 'y':
            webbrowser.open(link)
        elif open_link == 'n':
            break


def main():
    """
    Main function to run the news fetching program.
    """
    bold_start = "\033[1m"
    bold_end = "\033[0m"

    print("\033[5;31;40m")
    print(f"{bold_start}                 HERE YOU WILL GET ALL THE NEWS JUST IN ONE SEARCH                   {bold_end}\n")
    print(f"{bold_start}{time.asctime(time.localtime(time.time()))}{bold_end}")

    user_agent = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0"
    }

    topic = input(f"{bold_start}\n\033[1;35;40m Search any news (state, city, country, etc.): {bold_end} ").strip()

    news = fetch_news_times_of_india(topic, user_agent)
    display_news(news)
    if not news:
        print("Sorry, no news available.")

    print("\nThank you! 😊")


if __name__ == "__main__":
    main()
