import sqlite3
import time

from base import HackerNews


class HackerNewsSqlite(HackerNews):
    """
    This class extends HackerNews
    """
    def run(self):
        """
        This function creates a new db named hackernews.db and inserts data into it
        :return: true
        """
        conn = sqlite3.connect('hackernews.db')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS TOP_NEWS")
        print('**************** Dropped existing table ****************')
        create_table_sql = '''CREATE TABLE TOP_NEWS(id INT NOT NULL PRIMARY KEY,type CHAR(10),by VARCHAR(50),
        url VARCHAR,title VARCHAR)'''
        cursor.execute(create_table_sql)
        print('**************** Table created ****************')
        insert_sql = '''INSERT INTO TOP_NEWS VALUES(?,?,?,?,?)'''
        cursor.executemany(insert_sql, self.data)
        print('**************** {} Rows added ****************'.format(len(self.data)))
        conn.commit()
        conn.close()
        return True


start = time.time()
news_csv = HackerNewsSqlite().run()
end = time.time()
total_time = end - start
print('It took {} seconds to complete'.format(total_time))
print('Find the db file in the folder root!')
