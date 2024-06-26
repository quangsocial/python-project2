import requests
from bs4 import BeautifulSoup

# URL của trang bạn muốn kéo dữ liệu
url = 'https://1688.com'

# Gửi yêu cầu HTTP đến URL
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    # Sử dụng BeautifulSoup để phân tích cú pháp nội dung HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Tìm kiếm dữ liệu trong trang HTML dựa trên các thẻ và class của chúng
    # Ví dụ: tìm tất cả các phần tử có thẻ 'div' và class 'product-name'
    product_names = soup.find_all('div', class_='product-name')
    
    for product in product_names:
        print(product.text)
else:
    print('Không thể lấy dữ liệu từ URL nhé')