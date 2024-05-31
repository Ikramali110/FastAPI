from database import Base,engine
from models import Student

print("Creating database ....")

Base.metadata.create_all(engine)