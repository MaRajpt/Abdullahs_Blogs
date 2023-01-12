from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

sender = "testmail.rajpt6236@gmail.com"
password = "ooouzpnpmhrpuxdi"
receiver = "ma0880@outlook.com"

url ="https://www.amazon.com/Lenovo-Ideapad-Touchscreen-i3-1005G1-Processor/dp/B08B6F1NNR/ref=sxin_13_pa_sp_search_thematic_sspa?content-id=amzn1.sym.9c246b91-3d49-4e6c-8ff6-5b6e9a100bd4%3Aamzn1.sym.9c246b91-3d49-4e6c-8ff6-5b6e9a100bd4&crid=322TEJ0HL05LK&cv_ct_cx=laptop&keywords=laptop&pd_rd_i=B08B6F1NNR&pd_rd_r=e7777b0e-6714-43a6-a1c4-c830c70733fb&pd_rd_w=k2dmE&pd_rd_wg=WQPT3&pf_rd_p=9c246b91-3d49-4e6c-8ff6-5b6e9a100bd4&pf_rd_r=74P918YYB3QKFHZZN4SE&qid=1666162501&qu=eyJxc2MiOiIxMC43OSIsInFzYSI6IjEwLjQ3IiwicXNwIjoiOS43OCJ9&sprefix=lapto%2Caps%2C357&sr=1-1-a43b4223-fbe9-48b0-af69-6d70cf84978b-spons&psc=1"

response = requests.get(url, headers={'Accept-Language':'en-US,en;q=0.9,ar;q=0.8', "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"})
content = response.text

soup = BeautifulSoup(content, 'lxml')

tag = soup.find(name='span', class_= 'a-price-whole')

current_price = float(tag.text)

wanted_price = 400

if wanted_price > current_price:
    print('gg')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, f"Its {current_price} You have a Deal! ")


