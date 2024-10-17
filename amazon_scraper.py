import requests
from bs4 import BeautifulSoup
from api.app import db, create_app
from api.models import Product, Page, Review
from sqlalchemy.exc import IntegrityError
import time, random

class AmazonScraper:
    def __init__(self):
        self.base_url = 'https://www.amazon.com/s?k=watches&page='
        self.headers = {
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        self.scrapedata = list()

    def scrape_watches(self):
        print("Scraping started")
        last_page_scraped = Page.query.first()
        if not last_page_scraped:
            last = Page(last_page_scraped=1)
            db.session.add(last)
            db.session.commit()
            print("Last page scraped new data inserted")
        base_url = f"{self.base_url}{last_page_scraped.last_page_scraped}"
        response = requests.get(base_url, headers=self.headers)
        if response.status_code != 200:
            print(f"Failed to retrieve page: {response.status_code}")
            return
        soup = BeautifulSoup(response.content, 'html.parser')

        for item in soup.select('.s-result-item'):
            watch_data = {
                "brand": "",
                "model": "",
                "price": "",
                "url": "",
                "image": "",
                "specifications": "",
                "ratings": "",
            }
            try:
                brand = item.select_one('.a-size-base-plus').text
                price = item.select_one('.a-price-whole').text
                price = price.replace(',', '')  # Remove commas from price
                model = item.select_one('.a-text-normal').text
                image = item.select_one('.s-image').get('src')
                url = item.select_one('.a-text-normal').get('href')
                
                url = f"https://amazon.com{url.replace('amp;', '') if url else ''}"
                watch_data["brand"] = brand
                watch_data["price"] = price
                watch_data["model"] = model
                watch_data["image"] = image
                watch_data["url"] = url
                product_details = requests.get(url)
                if product_details.status_code == 200:
                    product_soup = BeautifulSoup(product_details.content, 'html.parser')
                    product_arr = product_soup.select('.a-list-item.a-size-base.a-color-base')
                    prod_rating = product_soup.select_one('.a-icon.a-icon-star.a-star-4-5.cm-cr-review-stars-spacing-big').text[0:3]
                    print('prod_rating: ',prod_rating)
                    specs = ''
                    for i in product_arr:
                        specs += f"{i.text}\n"
                    watch_data["specifications"] = specs
                    watch_data["ratings"] = prod_rating


                    price = watch_data["price"]+'0'
                    product = Product(
                        brand=watch_data["brand"],
                        model=watch_data["model"],
                        price=price,
                        image_url=watch_data["url"],
                        specifications=watch_data["specifications"],
                        ratings=watch_data["ratings"],
                    )
                    db.session.add(product)
                    db.session.commit() 
                    print('product id: ', product.id)
                    reviews = product_soup.select('.review')
                    for review in reviews:
                       
                        rating = float(review.select_one('.a-icon-alt').text.split()[0])
                        review_text = review.select_one('.review-text-content').text.strip() if review.select_one('.review-text-content') else ''
                        review_date = review.select_one('.review-date').text.strip() if review.select_one('.review-date') else ''
                        reviewer_name = review.select_one('.a-profile-name').text if review.select_one('.a-profile-name') else 'Anonymous'

                        new_review = Review(
                            product_id = product.id,
                            reviewer_name=reviewer_name,
                            review_text=review_text,
                            review_date=review_date,
                            rating=rating,
                        )
                        db.session.add(new_review)  
                        db.session.commit()    
            except:
                pass
            

            print(watch_data["brand"], "Inserted")
            random_delay = random.uniform(1, 5)
            time.sleep(random_delay)
        
        last = Page.query.first()
        last.last_page_scraped += 1

        db.session.add(last)
        db.session.commit()
        print("Last page scraped updated")
        
if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        a = AmazonScraper()
        a.scrape_watches()
        time.sleep(60*60)
