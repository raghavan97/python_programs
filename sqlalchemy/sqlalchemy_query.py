from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from sqlalchemy_declarative import Address, Base, Person
 
engine = create_engine('sqlite:///sqlalchemy_example.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
 
# Make a query to find all Persons in the database
persons = session.query(Person).all()
for p in persons:
    print p.id, p.name

# Return the first Person from all Persons in the database
person = session.query(Person).first()
print person.id, person.name

# Find all Address whose person field is pointing to the person object
address = session.query(Address).filter(Address.person == person).all()
for a in address:
    print a.street_name, a.street_number, a.post_code, a.person_id, a.person


# Retrieve one Address whose person field is point to the person object
address = session.query(Address).filter(Address.person == person).one()
print address.post_code
