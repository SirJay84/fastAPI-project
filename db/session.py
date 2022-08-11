from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session

# create an engine
SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/user/Documents/SirJayProjects/TechCamp/todo.db'
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False})

# create a configured "Session" class
SessionLocal = sessionmaker(bind=engine, autocommit = False, autoflush = False)

"""The SQLALCHEMY_DATABASE_URI - defines the file where SQLite will persist data."""
"""SQLAlchemy create_engine function - instantiates our engine, passing in the DB connection URI."""
"""The check_same_thread: False config - FastAPI can access the database with multiple threads in a single request,SQLite needs to be configured to allow that."""
"""DB Session - the session object is our main access point to the database."""