def get_headphones(soup):
    headphones = soup.select('div[class="_4ddWXP"]')
    #print(headphones)
    data = []
    for headphone in headphones:
        image_element = headphone.select_one('img')
        image_link = image_element['src'] if image_element else None
        title_element = headphone.select_one('a[class="s1Q9rs"]')
        title = title_element['title'] if title_element else None
        product_link = "https://flipkart.com"+title_element['href'] if title_element else None
        tags_element = headphone.select_one('div[class="_3Djpdu"]')
        tags = tags_element.text if tags_element else None
        rating_element = headphone.select_one('div[class="3Djpdu"]')
        rating = rating_element.text if rating_element else None
        total_ratings_element = headphone.select_one('span[class="_2_R_DZ"]')
        total_ratings = total_ratings_element.text.strip('()') if total_ratings_element else None
        sponsored_element = headphone.select_one('div[class="_4HTuuX"]')
        sponsored_status = "Yes" if sponsored_element else "No"
        price_element = headphone.select_one('div[class="_25b18c"]')
        
        if price_element:
            discounted_price = price_element.select_one('div[class="_30jeq3"]').text if price_element.select_one('div[class="_30jeq3"]') else None
            price = price_element.select_one('div[class="_3I9_wc"]').text if price_element.select_one('div[class="_3I9_wc"]') else None
            discount = price_element.select_one('div[class="_3Ay6Sb"]').text if price_element.select_one('div[class="_3Ay6Sb"]') else None
        
        else:
            discounted_price = price = discount = None

        fassured_element = headphone.select_one('div[class="_32g5_j"]')
        fassured_status = "Yes" if fassured_element else "No"

        headphone_data = {
            "title" : title,
            "tags" : tags,
            "sponsored_status" : sponsored_status,
            "rating" : rating,
            "rating_count" : total_ratings,
            "discounted_price" : discounted_price,
            "discount" : discount,
            "price" : price,
            "product_link" : product_link,
            "product_image" : image_link,
            "isFassured" : fassured_status,
        }

        data.append(headphone_data)
    return data