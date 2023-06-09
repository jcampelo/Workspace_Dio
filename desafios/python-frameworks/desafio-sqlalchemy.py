from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, func, select
from sqlalchemy import inspect
from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import String 
from sqlalchemy import ForeignKey
from sqlalchemy import select


Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    #atributos
    id = Column(Integer, primary_key= True )
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        
        "Address", back_populates="user", cascade = "all, delete-orphan" 
    
    )

    def __repr__(self):
       return f" User(id={self.id}, name={self.name}, fullname={self.fullname})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable = False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable = False)
    
    user = relationship("User", back_populates="address") 

    def __repr__(self):
      return f"Address(id={self.id}, email_address={self.email_address})"
        
# print(User.__tablename__)
# print(Address.__tablename__)


#conexão com o banco dados
engine =  create_engine("sqlite://")

#criando as classe como tabelas no banco de dado
Base.metadata.create_all(engine)


#depreciado - n se utliza mais(engine.table_names)
# print(engine.table_names)

#investiga o esquema do banco de dados
inspetor_engine = inspect(engine)

print(inspetor_engine.has_table("user_account"))

print(inspetor_engine.get_table_names())

print(inspetor_engine.default_schema_name)

#===============================================
with Session(engine) as session:

    juliana = User(
        name= 'juliana',
        fullname='Juliana Mascarenhas',
        address=[Address(email_address="julanam@email.com")]
    )

    Sandy = User(
        name= "Sandy",
        fullname= "Sandy Cardoso",
        address=[Address(email_address="sandy@email.br"),
                Address(email_address = " sandyc@gmail2.org")]

    )

    Patrick = User(

        name="Patrick",
        fullname="Patrick ribeirinho",
    )

    session.add_all([juliana, Sandy, Patrick])

    session.commit()


#STMT = STAMENTES

stmt = select(User).where(User.name.in_(["juliana", "sandy"]))
print("\nRecuperando usuario a partir de condição de filtragem")
for user in session.scalars(stmt):
    print(user)


stmt_address = select(Address).where(Address.user_id.in_([2]))
print("\nRecuperando emails de sandy")
for address in  session.scalars(stmt_address):
    print(address)

stmt_order = select(User).order_by(User.fullname.desc())
print("\nRecuperando info de maneira ordenada")
for result in session.scalars(stmt_order):
    print(result) 

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print(result)


connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("Executando statement a partir da connection")
for result in results:
    print(result)

stmt_count = select(func.count("*")).select_from(User)
print("\nTotal de instâncias em User")
for result in session.scalars(stmt_count ):
    print(result)