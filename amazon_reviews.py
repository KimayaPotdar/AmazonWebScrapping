# Importing Scrapy Library
import scrapy
 
# Creating a new class to implement Spide
class AmazonReviewsSpider(scrapy.Spider):
 
    # Spider name
    name = 'amazon_reviews'
 
    # Domain names to scrape
    allowed_domains = ['amazon.in']
 
    # Base URL for the MacBook air reviews
    # myBaseUrl = "https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/product-reviews/B073Q5R6VR/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&amp;amp;reviewerType=all_reviews&amp;amp;pageNumber="
    myBaseUrl = "https://www.amazon.in/GIORDANO-Cotton-Pollution-Reusable-Outdoor/product-reviews/B089FFMMMZ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&amp;amp;pageNumber="
    start_urls=[]
 
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,50):
        start_urls.append(myBaseUrl+str(i))
 
    # Defining a Scrapy parser
    def parse(self, response):
            ##cm_cr-review_list => holder box for comments (ignores other items on page)
            data = response.css('#cm_cr-review_list')

            #Collecting User details
            user_details = data.css('.a-profile-name')

            # Collecting product star ratings
            star_rating = data.css('.review-rating')

            # Collecting review title
            review_title = data.css('.review-title-content')

            # Collecting date of review
            review_date = data.css('.review-date')

            # Collecting user reviews
            comments = data.css('.review-text')
            count = 0
 
            # Combining the results
            for review in user_details:
                yield{
                    'user_details': ''.join(user_details[count].xpath(".//text()").extract()),
                    'star_rating': ''.join(star_rating[count].xpath(".//text()").extract()),
                    'review_title': ''.join(review_title[count].xpath(".//text()").extract()),
                    'review_date': ''.join(review_date[count].xpath(".//text()").extract()),
                    'comments': ''.join(comments[count].xpath(".//text()").extract())}
                count=count+1