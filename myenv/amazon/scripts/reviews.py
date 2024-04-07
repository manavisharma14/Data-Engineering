
def get_reviews(soup):
    review_elements = soup.select('div[data-hook="review"]')
    scraped_reviews = []
    
    for review in review_elements:
        author_review_element = review.select_one('span.a-profile-name')
        author_name = author_review_element.text if author_review_element else None
        ratings_element = review.select_one('i.a-icon-star')
        ratings_text = ratings_element.text if ratings_element else None
        if ratings_text:
            # Assuming the rating text might be in format: "4.0 out of 5 stars"
            ratings = ratings_text.split(' out of 5 stars')[0]
        else:
            ratings = None
        
        title_element = review.select_one("a.review-title")
        title_span_element = title_element.select_one("span:not([class])") if title_element else None
        title = title_span_element.text if title_span_element else None
        
        content_element = review.select_one("span.review-text")
        content = content_element.text if content_element else None
        
        date_element = review.select_one("span.review-date")
        review_date = date_element.text if date_element else None
        
        verified_element = review.select_one("span.a-size-mini")
        verified = verified_element.text if verified_element else None
        
        image_element = review.select_one("img.review-image-tile")
        image = image_element.attrs['src'] if image_element else None 


        r = {
            "author": author_name,
            "rating": ratings, 
            "title": title, 
            "content": content,
            "date": review_date, 
            "verified": verified, 
            "image_url": image 
        }

        scraped_reviews.append(r)
    return scraped_reviews
