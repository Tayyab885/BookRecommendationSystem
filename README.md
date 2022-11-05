# BookRecommendationSystem
> https://tayyab885-bookrecommendationsystem-recommendation-zecywg.streamlit.app/
### Website Preview
#### Home Page:
<img src="Images/home.png" width="1000">

#### Recommended Page:
<img src="Images/4u.png" width="1000">

----

## Installation: 📦
>pip install -r requirements.txt

#### Clone:

- Clone this repo to your local machine.

#### Run app locally:
Open terminal in the directory where app is cloned and run the following command in terminal.
```shell
$ streamlit run Recommendation.py
```

## Features 📋
* User can search through various books and look through its details.
* User can get the top most rated books.
* User can get book recommendation (Recommendation algorithm (Collaborative Filtering) which suggests new books based on the ratings given by user.)
---

## Algorithm
##### Collabortive Filtering (Recommender Algorithm)
* Collaborative filtering filters information by using the interactions and data collected by the system from other users. It's based on the idea that people who agreed in their evaluation of certain items are likely to agree again in the future.
* When we want to find a new book to read we'll often ask our friends for recommendations. Naturally, we have greater trust in the recommendations from friends who share tastes similar to our own.
* Collaborative-filtering systems focus on the relationship between users and items. The similarity of items is determined by the similarity of the ratings of those items by the users who have rated both items.
* There are two types of collaborative filtering
    * **User-based**, which measures the similarity between target users and other users.
    * **Item-based**, which measures the similarity between the items that target users rate or interact with and other items.
    > I have used **user based** collaborative filtering in this project.
    
    
    
  ---
