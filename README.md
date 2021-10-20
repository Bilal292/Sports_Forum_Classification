# text-classification

The folder called 'webProject' is the website that uses classification model to classify the posts
In order to it run the website on your localhost, you can cd into the folder from your terminal and run: 
```python manage.py runserver```
If you get some errors, it could be because of the missing libraries. I have included the requirements.txt file

The folder Classifiers&TwitterAPI includes the code for collecting the dataset
and the code for both naive bayes and logistic regression classification models
These files can be opened in jupyter notebook.
To run the TwitterTweets jupyter notebook code, you might need to install tweepy

The dataset can be found in webProject/forum, and in Classifiers&TwitterAPI, its named data.csv.