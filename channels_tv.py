import requests
from bs4 import BeautifulSoup

url = 'https://www.channelstv.com/category/sports/'
tri = requests.get(url)
if tri.status_code == 200:
    soup = BeautifulSoup(tri.text, 'html.parser')
    for data in soup.find_all('article'):
        title = data.find('h3',{'class': "post-title"})
        if title:
            title_text = title.text.strip()
            print(title_text)
        img = data.find('img')
        if img:
            image = img.get('src')
        else:
            print('404')
        print('\n')
        
#         if title :
#             title_text = title.text.strip()
#             print('Title:', title_text)
#         else:
#             print('Titlt; Not found')
            
#         # img = data.find('img') 
#         if img:
#             image = img.get('src')
#             print('Iitle URL:', image)
#         else:
#             print('Image URL: Not found')
            
# else:
#     print('Invalid URL')


