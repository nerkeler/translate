import sqlite3, os


class WordRecordMapper:
    def __init__(self, db_file):
        self.db_file = db_file
        if not os.path.exists("word_records.db"):
            self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # 创建 word_records 表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS word_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                word TEXT NOT NULL,
                definition TEXT NOT NULL,
                example TEXT,
                pronunciation TEXT,
                category TEXT,
                source TEXT,
                progress INTEGER,
                occurrence INTEGER,
                familiar BOOLEAN,
                created_at DATETIME,
                updated_at DATETIME
            )
        ''')

        conn.commit()
        conn.close()

    def insert_record(self, record):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # 插入记录
        cursor.execute('''
            INSERT INTO word_records (
                word, definition, example, pronunciation, category, source,
                progress, occurrence, familiar, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            record.word, record.definition, record.example, record.pronunciation,
            record.category, record.source, record.progress, record.occurrence,
            record.familiar, record.created_at, record.updated_at
        ))

        conn.commit()
        conn.close()
