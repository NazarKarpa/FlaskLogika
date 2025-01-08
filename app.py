from flask import Flask, render_template, request, flash
from dotenv import load_dotenv
from db_scripts import *
import os
load_dotenv()


app = Flask(__name__)  # Створюємо веб–додаток Flask

db = DataBaseManager('orders_db.db')

IMG_PATH = os.path.dirname(__file__) + os.sep + 'static' + os.sep + 'img'


@app.context_processor
def get_categories():#r
    categories = db.get_all_categories()
    return dict(categories = categories)

@app.route("/")  # Вказуємо url-адресу для виклику функції
def index():
    articles = db.get_all_articles()
    return render_template("index.html", articles=articles) # html-сторінка, що повертається у браузер

@app.route('/articles/<int:article_id>')
def article_page(article_id):
    article = db.get_article(article_id)
    return render_template('article_page.html', article=article)

@app.route('/category/<int:category_id>')
def category_page(category_id):
    article = db.get_category_articles(category_id)
    return render_template('index.html', articles=article)


@app.route('/articles/new', methods=['GET', 'POST'])
def new_article():
    if request.method == 'POST':#якщо користувач надсилає форму
       # if request.form['category'] != 'Виберіть категорію':
         #   image = request.files['image'] #получаємо файл картинки
         #   image.save(IMG_PATH + image.filename)
         #   db.add_article(request.form['title'], request.form['content'], image.filename, 1, request.form['category'])
         flash('Ми вам передзвонимо', 'alert-success')
        #else:
         #flash('Заповніть всі поля і статтю вибріть')
    return render_template('new_article.html')

@app.route("/search")  # Вказуємо url-адресу для виклику функції
def search():
    articles = db.get_all_articles()
    if request.method == 'GET':
        query= request.args.get('query')
        articles = db.search_article(query)

    return render_template("index.html", articles=articles) # html-сторінка, що повертається у браузер


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)  # Запускаємо веб-сервер з цього файлу в режимі налагодження
