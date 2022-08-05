import requests

url = "https://www.indeed.com/jobs?q=Software Developer&l=Charlotte"

payload={}
headers = {
  'Cookie': 'CTK=1g9ltl5schapt800; __cf_bm=lWL02xhVtRafXcUxCUnUfSj31QEa4Onp9dawaLlgGbQ-1659666864-0-AbZSaLu9imvK4tGq02N7XNGhyVnGVS7yMvlTIOlKpAemkLmgDMCAxxwxBtMeJtG53gkVus1Ij68kBlmEn4w8psM=; _cfuvid=w8EYFZYer21Cqw_MLHuHcerD7Sx9d6JUYKlTFrGhqX0-1659666864162-0-604800000; INDEED_CSRF_TOKEN=ciXw5WnjLRB4JaTJPruxOf63xk2fd8XA; JSESSIONID=D7BAFCBB06C58981C84F604AE511259D; PREF="TM=1659666864024:L=Charlotte"; RQ="q=Software+Developer&l=Charlotte&ts=1659666864050"; UD="LA=1659666864:CV=1659666864:TS=1659666864:SG=f11ba72e208a41159fed7c4bb7483033"; ctkgen=1; indeed_rcc=""; jaSerpCount=1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
