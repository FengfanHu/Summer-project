# Summer-project
This is the code repository of the thesis "Argumentation Driven Preference Identification and Recommendation".

## Dataset
Yelp: https://www.yelp.com/dataset

## Notebooks
- 1.Data processing.ipynb
  - Data preprocessing  
  `INPUT`: Yelp dataset (business, reviews)  
  `OUTPUT`: restaurants_reviews, users_reviews
- 2.Aspect based sentiment analysis.ipynb
  - Data preprocessing  
  - Aspect extraction  
  - Sentiment analysis  
  `INPUT`: restaurants_reviews, users_reviews  
  `OUTPUT`: restaurants_reviews_with_aspects_polarities, users_reviews_with_aspects_polarities
- 3.Model.ipynb
  - User profile building
  - Restaurant profile building
  - Recommendation
  - Analysis  
  `INPUT`: restaurants_reviews, users_reviews
