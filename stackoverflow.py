import requests
from bs4 import BeautifulSoup

URL="https://stackoverflow.com/jobs?q=python"

def get_last_page():
  result= requests.get(URL)
  soup= BeautifulSoup(result.text,"html.parser" )
  pages=soup.find("div", {"class":"s-pagination"}).find_all("a")
  last_pages =int(pages[-2].text)
  return last_pages
  #last_pages=pagnition.find("")
  #print(link)


def extract_job(html):
  if (html.find("h2") and html.find("h3")):
    title= html.find("h2").get_text(strip=True)
    #print(title)

    #companies= html.find("h3").find_all("span")
    #company_name=companies[0].get_text(strip=True)
    #company_loc=companies[1].get_text(strip=True)
    
    company_name, company_loc = html.find("h3").find_all("span", recursive=False)
    
    #print(company_name.get_text(strip=True), company_loc.get_text(strip=True))


    id=html.find("button")["data-id"]
    link=f"https://stackoverflow.com/jobs/{id}"
    #print(id)

    return {'title':title, 'company': company_name.get_text(strip=True), 'location':company_loc.get_text(strip=True), 'link':link}
  

def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"scrapping page{page+1}")
    result= requests.get(f"{URL}&pg={page+1}")
    soup=BeautifulSoup(result.text,"html.parser")
    results=soup.find_all("div","grid")
    #print(results)

    for result in results:
      #print(result)
      job= extract_job(result)
      jobs.append(job)
  return jobs 


def get_jobs():
  last_page=get_last_page()
  #print (last_page)
  jobs=extract_jobs(last_page)
  return jobs

