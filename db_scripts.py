import sqlite3

class DataBaseManager:
    def __init__(self, dname):
        self.conn = None
        self.cursor = None
        self.dname = dname


    def open(self):
        self.conn = sqlite3.connect(self.dname)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()



    def get_all_articles(self):
        self.open()
        self.cursor.execute('''SELECT * FROM Articles''')
        data = self.cursor.fetchall()
        self.close()
        return data


    def get_article(self, article_id):
        self.open()
        self.cursor.execute('''SELECT * FROM Articles WHERE id=?''', [article_id])
        data = self.cursor.fetchone()
        self.close()
        return data


    def get_all_categories(self):
        self.open()
        self.cursor.execute('''SELECT * FROM Categories''')
        data = self.cursor.fetchall()
        self.close()
        return data


    def get_category_articles(self, category_id):
        self.open()
        self.cursor.execute('''SELECT * FROM articles WHERE category_id=?''', [category_id])
        data = self.cursor.fetchall()
        self.close()
        return data


    def add_article(self, title,content, image, user_id, category_id):
        pass
        #Стровити функцію для додавання статті + сайт