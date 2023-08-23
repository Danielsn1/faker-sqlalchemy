from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.sqlite import DATE as SQLITE_DATE
from sqlalchemy import (
    Column,
    ForeignKey,
    MetaData,
    ARRAY,
    BIGINT,
    BigInteger,
    BINARY,
    BLOB,
    BOOLEAN,
    Boolean,
    CHAR,
    CLOB,
    DATE,
    Date,
    DATETIME,
    DateTime,
    DECIMAL,
    Enum,
    FLOAT,
    Float,
    INT,
    INTEGER,
    Integer,
    Interval,
    JSON,
    LargeBinary,
    NCHAR,
    NUMERIC,
    Numeric,
    NVARCHAR,
    PickleType,
    REAL,
    SMALLINT,
    SmallInteger,
    String,
    TEXT,
    TIME,
    Time,
    TIMESTAMP,
    TypeDecorator,
    Unicode,
    UnicodeText,
    VARBINARY,
    VARCHAR,
    Table
)

Base = declarative_base()
metadata = MetaData()

__all__ = (
    "Base",
    "Model",
    "RelationshipModel",
    "TypeOverrideModel",
)

model = Table(
    'model', metadata,
    Column('id', Integer, primary_key=True),
    Column('big_integer', BigInteger),
    Column('boolean',Boolean),
    Column('date', Date),
    Column('datetime', DateTime),
    # enumeration = Column(Enum)
    Column('float', Float),
    Column('integer', Integer),
    Column('interval', Interval),
    Column('json', JSON),
    Column('large_binary', LargeBinary),
    Column('numeric', Numeric),
    # pickle_type = Column(PickleType)
    Column('time', Time),
    # tuple_type = Column(TupleType)
    Column('small_integer', SmallInteger),
    Column('string', String),
    Column('unicode', Unicode),
    Column('unicode_text', UnicodeText)
)

class Model(Base):
    __tablename__ = "model"

    id = Column(Integer, primary_key=True)

    big_integer = Column(BigInteger)
    boolean = Column(Boolean)
    date = Column(Date)
    datetime = Column(DateTime)
    # enumeration = Column(Enum)
    float = Column(Float)
    integer = Column(Integer)
    interval = Column(Interval)
    json = Column(JSON)
    large_binary = Column(LargeBinary)
    numeric = Column(Numeric)
    # pickle_type = Column(PickleType)
    time = Column(Time)
    # tuple_type = Column(TupleType)
    small_integer = Column(SmallInteger)
    string = Column(String)
    unicode = Column(Unicode)
    unicode_text = Column(UnicodeText)


class RelationshipModel(Base):
    __tablename__ = "relationship_model"

    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey("model.id"))

    value = Column(String)

    model = relationship(Model, cascade="all")


class TypeOverrideModel(Base):
    __tablename__ = "type_override_model"

    id = Column(Integer, primary_key=True)

    sqlite_date = Column(SQLITE_DATE)
