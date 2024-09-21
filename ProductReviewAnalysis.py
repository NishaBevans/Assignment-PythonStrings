#Task 1: Keyword Highlighter: Write a program that searches through reviews list and looks for keywords such as "good", "excellent", 
#"bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords 
#in uppercase so they stand out.

def highlight_keywords(reviews, keywords):
    highlighted_reviews = []
    
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        highlighted_reviews.append(review)
    
    return highlighted_reviews


reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]


keywords = ["good", "excellent", "bad", "poor", "average"]


highlighted_reviews = highlight_keywords(reviews, keywords)


for review in highlighted_reviews:
    print(review)

#Task 2: Sentiment Tally: Develop a function that tallies the number of positive and negative words in each review.  The function should return 
#the total count of positive and negative words.

def tally_sentiment(reviews):
    positive = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]  
    negative = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

    positive_count = 0
    negative_count = 0

    for review in reviews:
        words = review.lower().split()
        for word in words:
             if word in positive:
                 positive_count += 1
             elif word in negative:
                negative_count += 1
    return positive_count, negative_count

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
positive_count, negative_count = tally_sentiment(reviews)

print(f"Total positive remarks: {positive_count}")
print(f"Total negative remarks: {negative_count}")

#Task 3: Review Summary: Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
#Ensure that the summary does not cut off in the middle of a word.

reviews_copy = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]

review_edit = reviews_copy[0][0:32]
print(review_edit + "...")
review_edit = reviews_copy[1][0:31]
print(review_edit + "...")
review_edit = reviews_copy[2][0:32]
print(review_edit + "...")
review_edit = reviews_copy[3][0:30]
print(review_edit + "...")
review_edit = reviews_copy[4][0:32]
print(review_edit + "...")