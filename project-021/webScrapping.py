# https://id.wikipedia.org/wiki/Niccol%C3%B2_Machiavelli

import requests
from bs4 import BeautifulSoup

def getWikipediaTopic(topic):
    url  = f"https://id.wikipedia.org/wiki/{topic.replace(' ','_')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"failed to retrieve data {response.status_code}")
        return None

def getArticleTitle(soup):
    return soup.find('h1').text

def getArticleSummary(soup):
    paragraphs = soup.find_all('p')
    for para in paragraphs:
        if para.text.strip():
            return para.text.strip()
    return "No summary found"

def getHeadings(soup):
    headings = [heading.text.strip() for heading in soup.find_all(['h2','h3','h4'])]
    return headings

def getRelatedLinks(soup):
    links = []
    for a_tag in soup.find_all('a',href = True):
        href = a_tag['href']
        if href.startswith('/wiki/') and ":" not in href:
            links.append(f"https://id.wikipedia.org{href}")
    return list(set(links))[:5]

def main():
    topic = input("Enter topic : ")
    page_content = getWikipediaTopic(topic)
    
    if page_content:
        soup = BeautifulSoup(page_content,'html.parser')
        title = getArticleTitle(soup)
        summary = getArticleSummary(soup)
        headings = getHeadings(soup)
        related_links = getRelatedLinks(soup)
        
        print("\n-Wikipedia Article detail-")
        print(f"\nTitle : {title}")
        print(f"\nSummary : {summary}")
        print(f"\nHeadings:")
        for heading in headings[:5]:
            print(f"- {heading}")
            
        print("\nRelated Links:")
        for link in related_links:
            print(f"-{link}")

#Run Program
if __name__ == "__main__":
    main()