import pandas as pd
import string
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("forum/data.csv")
data['NUM_CATEGORY']=data.category.map({'cricket':0,'football':1,'basketball':2,'hockey':3,'tennis':4, 'volleyball':5, 'tabletennis':6, 'baseball':7, 'rugby':8, 'badminton':9})
data.head()

def data_preprocessing(text):
    #this line removes unnecesary punctuation for example "!","," and splits the text in characters
    remove_punct = [char for char in text if char not in string.punctuation]
    
    remove_punct=''.join(remove_punct) #joining characters back into words
    
    #this will tokenize the text and remove stop words 
    return [word for word in remove_punct.split() if word.lower() not in stopwords.words('english')]

#This will split the dataset, so we will have 60% training set and 40%  test set randomised
x_train, x_test, y_train, y_test = train_test_split(data.text, data.NUM_CATEGORY, random_state=50)

#coverting the dataset into bag of words
#making it use the pre-processing function defined earlier
vect = CountVectorizer(analyzer=data_preprocessing) 
X_train = vect.fit_transform(x_train)
X_test = vect.transform(x_test)


classifier = MultinomialNB(alpha =0.2)
classifier.fit(X_train,y_train) #training the classifier


def predict_category(text): #takes a post

    test = vect.transform(text)   #feature extraction for the post
    predicted = classifier.predict(test)  #predicts post category
    
    #retunrs the predicted category name
    if predicted  == 0:
         return 'Cricket'
    elif predicted == 1:
        return 'Football'
    elif predicted == 2:
        return 'Basketball'
    elif predicted == 3:
        return 'Hockey'
    elif predicted == 4:
        return 'Tennis'
    elif predicted == 5:
        return 'Volleyball'
    elif predicted == 6:
        return 'Table Tennis'
    elif predicted == 7:
        return 'Baseball'
    elif predicted == 8:
        return 'Rugby'
    elif predicted == 9:
        return 'Badminton'
    else:
        return 'no class found'
