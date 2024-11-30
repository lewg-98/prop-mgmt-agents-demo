from app.database import DatabaseConnection
from app.database_operations import Database

DatabaseConnection.initialize_pool()

db = Database()

