import sqlite3


class DatabaseManager:
    def __init__(self, filename: str):
        self.conn = sqlite3.connect(filename, check_same_thread=False)
        self.cursor = self.conn.cursor()

    async def create_tables(self) -> None:
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS coinflips (id INTEGER PRIMARY KEY AUTOINCREMENT, result TEXT)"
        )
        self.conn.commit()

    async def save_result(self, result: str) -> None:
        self.cursor.execute("INSERT INTO coinflips (result) VALUES (?)", (result,))
        self.conn.commit()

    async def get_history(self) -> list:
        self.cursor.execute("SELECT result FROM coinflips")
        return self.cursor.fetchall()
