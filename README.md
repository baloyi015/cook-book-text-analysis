**Title:** Cookbook Review Text Analysis: Understanding User Opinions on Recipes

**Abstract:** This project explores user sentiment towards recipes using text analysis of cookbook reviews. The goal was to gain insights into user preferences and behavior. Techniques included data exploration, and text preprocessing.

**Introduction:**

Text analysis plays an important role in detecting and identifying user's sentiment towards something. In recipe domain, text analysis can help mitigate negative sentiments aimed at particular products by learning what works and what doesn't. To ensure robust recommendation systems are built, extensive text analysis should be conducted.

**Data:** The dataset can be downloaded from Kaggle, namely [Cookbook Reviews](https://www.kaggle.com/datasets/motahareshokri/cookbook-reviews).

**Data Preprocessing:** 
The following steps were conducted for data cleaning and formatting:
  - Load the "Cookbook Reviews" dataset (.csv file).
  - Convert timestamps to date format
  - Remove ratings with zero score
  - Rename colums `rec_nm`, `user_reput` and `response_no`
  - Remove columns `rec_cd`, `rec_no`, `cmt_id`, `user_id`, `user_nm`, `timestamp` and `datetime`
  - Remove dupplicated data points
  - Remov missing data points
  - Add `year` and `month` columns
  - Add user's sentiment column
  - Upvoted: remove ratings below or equal to 3
  - Downvoted: remove ratings above 3
  - Change downvoted values to negative signs(for plots)
  - Remove ratings 1-3 for positive sentiments
  - Remove ratings 4-5 for negative sentiments

**Exploratory Data Analysis (EDA):**
  - Recipe rating scores on monthly basis
  - Ratings per sentiment
  - Recipe accumulated ratings
  - Ratings per comment responses
  - Up and Down votes per rating score
  - Recipe rating and sentiment distributions

**Text Preprocessing:**
  - Convert text to lowercase 
  - Change words to correct contraction form 
  - Remove numbers from text 
  - Remove punctuations
  - Remove stopword 
  - Remove characters lower than 2
  - Lemmatize words to root form
  - Tokenize sentences

 **Text Analysis:**
- Association between different fields
- Document and sentence distributions
- Reviewed words associated with 1-3 and 4-5 ratingss v. negative, neutral and postive sentiments
- Identified most common words for each group(ratings and sentiments)

**Python libraries:** 
  - Data analysis (`nltk, spacy, scikit-learn`)
  - Visualization (`plotly, matplotlib, seaborn, wordcloud`).