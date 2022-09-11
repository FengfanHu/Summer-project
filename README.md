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
  - LCF-ATEPC (Powered by PyABSA)
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

## Note
Please note that the 2.Aspect based sentiment analysis.ipynb notebook works slowly, you can use GPU to accelerate this process by replacing the `auto_device` of `aspect_extractor = ATEPCCheckpointManager.get_aspect_extractor(checkpoint='english', auto_device=False)` to `True`.

## Acknowledgement
I write here to acknowledge [Yang Heng](https://github.com/yangheng95) for providing state-of-art aspect-based-sentiment-analysis tools: [PyABSA](https://github.com/yangheng95/PyABSA).
