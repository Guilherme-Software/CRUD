from sqlalchemy import create_engine, Column, String, select, update, delete
from sqlalchemy.orm import sessionmaker, declarative_base

#creating connection
engine = create_engine(f"mysql+pymysql://user:password@host/database")

try:
    with engine.connect() as connect:
        print("Connected!")

except Exception as er:
    print(f"Erro: {er}")

Base = declarative_base()


#map to the table
class Register(Base):
    __tablename__ = 'register'
    user = Column(String(100),primary_key=True, nullable=False)
    email = Column(String(100), unique = True, nullable=False)
    password = Column(String(100), nullable=False)

Base.metadata.create_all(engine)

#session maker
Session = sessionmaker(bind=engine)
session = Session()


#Create user
def register_user():
    user = input("User: ")
    email = input("E-mail: ")
    password = input("Password: ")

    new_register = Register(user=user,email=email, password=password)

    #register
    session.add(new_register)
    try:
        session.commit()
        print("User registered!")

    except Exception as us:
        print(f"Error: {us}")


#Read user
def read_user():
    username = input('You wanna read one user or all of them? Say the user name or all. ')
    if username == "all":
        search = session.query(Register).all()
        for row in search:
            print(f"User: {row.user}")
            print(f"E-mail: {row.email}")
            print(f"Password: {row.password}")
            print()

    else:
        query = select(Register).where(Register.user == username)
        result = session.execute(query).scalars().all()

        if result:
            for row in result:
                print(f"user: {row.user}")
                print(f"e-mail: {row.email}")
                print(f"password: {row.password}")

        else:
            print("Error, user not founded.")
        
    session.close()


#Update user
def update_user():
    upUser = input("What user you want change the password? Insert user: ")
    newpassword = (
        update(Register)
        .where(Register.user == upUser)
        .values(password = input("New password: "))
    )
    try:
        session.execute(newpassword)
        session.commit()
        print("Password chaged!")

    except Exception as eror:
        print(f"Error: {eror}")

    session.close()


#delete user
def delete_user():
    user_del = input("What user you want to delete? ")
    result = (
        delete(Register)
        .where(Register.user == user_del)
    )
    
    try:
        session.execute(result)
        session.commit()
        print(f"User {user_del} was been deleted!")

    except Exception as Derr:
        print(f"Error: {Derr}.")

    session.close()


#User question:
while True:
    wh = input("What you want to do? Create, Read, Update or Delete. Or type None to stop. ").lower()
    if wh == 'create':
        register_user()
    elif wh == 'read':
        read_user()
    elif wh == 'update':
        update_user()
    elif wh == 'delete':
        delete_user()
    elif wh == 'none':
        print(" Stopped!")
        break
    else:
        print("typed wrong! Try again")
