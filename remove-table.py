import sqlite3
DatabaseConnection = sqlite3.connect("AuthLog.db")
DatabaseCutsor = DatabaseConnection.cursor()
DatabaseCutsor.execute("DROP TABLE IF EXISTS AuthLogs")