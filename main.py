from newspaper import Article
from textblob import TextBlob
import nltk

#nltk.download('punkt_tab')

link_url = "https://en.wikipedia.org/wiki/Newspaper"
article = Article(link_url)

# Download, parse, and apply NLP tasks on the article
article.download()  #article from the web
article.parse()     #removal html tags
article.nlp()       #nlp processing if required

# Extract text now  
text = article.text  # Get full article text 
summary = article.summary  # Get the article summary

print("Article Text: ")
print(text)
#print("\nArticle Summary: ")
#print(summary)

tblob = TextBlob(summary) #create textblob obj from text
print('\n')
sentiment = tblob.sentiment.polarity #gives us a score -1 to 1 , neg to pos
print(sentiment)

#check with a slightly negative article

#url_neg ='https://www.nytimes.com/topic/subject/murders-and-attempted-murders'
#artic = Article(url_neg)
#artic.download()  
#artic.parse()     
#artic.nlp()

#summ=artic.summary
#print(summ)
#tblobb = TextBlob(summ) #create textblob obj from text
#print('\n')
#senti = tblobb.sentiment.polarity #gives us a score -1 to 1 , neg to pos
#print(senti)


#func for choice of text reading

def func(): #file has really neg text written
    with open("file.txt",'r') as reader:
        text = reader.read()
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    print(sentiment)
    
func()