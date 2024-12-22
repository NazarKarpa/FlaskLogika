from flask import Flask, render_template
from db_scripts import DataBaseManager


app = Flask(__name__)  # Створюємо веб–додаток Flask
db = DataBaseManager('orders_db.db')

@app.context_processor
def get_categories():
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
    return render_template('new_article.html')



if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)  # Запускаємо веб-сервер з цього файлу в режимі налагодження
