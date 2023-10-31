from flask import Flask, jsonify, request
import pandas as pd

articles_data = pd.read_csv('articles.csv')
all_articles = articles_data[['url' , 'title' , 'text' , 'lang' , 'total_events']]
liked_articles = []
not_liked_articles = []

app = Flask(__name__)

def assign_val():
    m_data = {
        "url": all_articles.iloc[0,0],
        "title": all_articles.iloc[0,1],
        "text": all_articles.iloc[0,2] or "N/A",
        "lang": all_articles.iloc[0,3],
        "total_events": all_articles.iloc[0,4]
    }
    return m_data

# API para exibir o primeiro artigo
@app.route("/get-article")
def get_article():

    return files.downloads('article.csv')


# API para mover o artigo para a lista de artigos curtidos
@app.route("/liked-article")
def liked_article():

    return files.download('liked_article')


# API para mover o artigo para a lista de artigos não curtidos
@app.route("/unliked-article")
def unliked_article():

    return filoes.download('unliked_article')

# execute o aplicativo
if __name__ == "__main__":
    app.run()
