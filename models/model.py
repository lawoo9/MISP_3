from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime
from typing import Optional

class Base(DeclarativeBase):
    pass

class BaseModel:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

class Base(DeclarativeBase):
    pass

class User(Base, BaseModel):
    __tablename__ = 'user'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username:Mapped[str] = mapped_column(String(200), unique=True)
    password:Mapped[str] = mapped_column(String(255))

class ClientProfile(Base, BaseModel):
    __tablename__ = 'client_profile'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    created_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    updated_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    unique_id:Mapped[str] = mapped_column(String(100), unique=True)
    first_name:Mapped[str] = mapped_column(String(100))
    middle_name:Mapped[Optional[str]] = mapped_column(String(100))
    last_name:Mapped[str] = mapped_column(String(100))
    date_of_birth:Mapped[datetime] = mapped_column(DateTime)
    country_of_birth:Mapped[str] = mapped_column(String(100))
    gender:Mapped[str] = mapped_column(String(100))
    marital_status:Mapped[str] = mapped_column(String(100))
    occupation:Mapped[str] = mapped_column(String(100))
    gender_identity:Mapped[str] = mapped_column(String(100))
    sexual_orientation:Mapped[str] = mapped_column(String(100))
    phone_number:Mapped[Optional[str]] = mapped_column(String(100))
    address:Mapped[Optional[str]] = mapped_column(String(100))
    city:Mapped[Optional[str]] = mapped_column(String(100))
    state:Mapped[Optional[str]] = mapped_column(String(100))
    zip_code:Mapped[Optional[str]] = mapped_column(String(100))
    country:Mapped[Optional[str]] = mapped_column(String(100))
    email:Mapped[Optional[str]] = mapped_column(String(100))
    ethnicity:Mapped[Optional[str]] = mapped_column(String(100))
    race:Mapped[Optional[str]] = mapped_column(String(100))

class CustomerInformation(BaseModel, Base):
    __tablename__ = "customer_information"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    created_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    updated_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
    Customer_Lastname: Mapped[Optional[str]] = mapped_column(String(64))
    Customer_Firstname: Mapped[Optional[str]] = mapped_column(String(64))
    Customer_Lastname: Mapped[Optional[str]] = mapped_column(String(64))
    Customer_Middlename: Mapped[Optional[str]] = mapped_column(String(64))
    Customer_date_of_birth: Mapped[datetime] = mapped_column(DateTime)
    Customer_Estimated_delivery_date: Mapped[datetime] = mapped_column(DateTime)
    Customer_Address: Mapped[Optional[str]] = mapped_column(String(64))
    Residency_of_Customer: Mapped[Optional[str]] = mapped_column(String(64))
    Customer_State: Mapped[Optional[str]] = mapped_column(String(100))
    Customer_Zip: Mapped[Optional[str]] = mapped_column(String(100))
    Customer_telephone_Number: Mapped[Optional[str]] = mapped_column(String(100))
    Customer_type_of_insurance: Mapped[Optional[str]] = mapped_column(String(100))
    Customer_Race: Mapped[Optional[str]] = mapped_column(String(100))
    Hispanic: Mapped[Optional[str]] = mapped_column(String(100))
    Customer_country_of_birth: Mapped[Optional[str]] = mapped_column(String(100))
    Customer_Primary_Language: Mapped[Optional[str]] = mapped_column(String(100))
    Check_if_interpreter_is_needed: Mapped[Optional[str]] = mapped_column(String(100))

    class GuarantorInformation(BaseModel, Base):
     __tablename__ = "Guarantor_information"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    created_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    updated_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("customer_information.Guarantor_unique_id", onupdate="CASCADE", ondelete="CASCADE"))
    Guarantor_Address: Mapped[Optional[str]] = mapped_column(String(64))
    Guarantor_Residency: Mapped[Optional[str]] = mapped_column(String(64))
    Guarantor_State: Mapped[Optional[str]] = mapped_column(String(100))
    Guarantor_Zip: Mapped[Optional[str]] = mapped_column(String(100))
    Guarantor_telephone_Number: Mapped[Optional[str]] = mapped_column(String(100))
    Guarantor_type_of_insurance: Mapped[Optional[str]] = mapped_column(String(100))
    Guarantor_Race: Mapped[Optional[str]] = mapped_column(String(100))
    Guarantor_Hispanic: Mapped[Optional[str]] = mapped_column(String(100))
    Guarantor_country_of_birth: Mapped[Optional[str]] = mapped_column(String(100))
    Guarantor_Primary_Language: Mapped[Optional[str]] = mapped_column(String(100))

    class EmployeeRecords(BaseModel, Base):
     __tablename__ = "employee_records"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    created_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    updated_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
    Employee_Lastname: Mapped[Optional[str]] = mapped_column(String(64))
    Employee_Firstname: Mapped[Optional[str]] = mapped_column(String(64))
    Employee_Middlename: Mapped[Optional[str]] = mapped_column(String(64))
    Employee_date_of_birth: Mapped[datetime] = mapped_column(DateTime)
    Employee_Estimated_delivery_date: Mapped[datetime] = mapped_column(DateTime)
    Employee_Address: Mapped[Optional[str]] = mapped_column(String(64))
    Residency_of_Employee: Mapped[Optional[str]] = mapped_column(String(64))
    Employee_State: Mapped[Optional[str]] = mapped_column(String(100))
    Employee_Zip: Mapped[Optional[str]] = mapped_column(String(100))
    Employee_telephone_Number: Mapped[Optional[str]] = mapped_column(String(100))
    Employee_type_of_insurance: Mapped[Optional[str]] = mapped_column(String(100))
    Employee_Race: Mapped[Optional[str]] = mapped_column(String(100))
    Employee_Hispanic: Mapped[Optional[str]] = mapped_column(String(100))
    Employee_country_of_birth: Mapped[Optional[str]] = mapped_column(String(100))
    Employee_Primary_Language: Mapped[Optional[str]] = mapped_column(String(100))
    Employee_Check_if_interpreter_is_needed: Mapped[Optional[str]] = mapped_column(String(100))

    class FinancialData(BaseModel, Base):
     __tablename__ = "financial_data"
     id: Mapped[int] = mapped_column(Integer, primary_key=True)
     created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
     updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
     created_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
     updated_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
     unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
     Balance_For_January_BD: Mapped[Optional[str]] = mapped_column(String(64))
     January_BD: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_Feburary_BD: Mapped[Optional[str]] = mapped_column(String(64))
     Feburary_BD: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_March_BD: Mapped[Optional[str]] = mapped_column(String(64))
     March_BD: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_April_BD: Mapped[Optional[str]] = mapped_column(String(64))
     April_BD: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_May_BD: Mapped[Optional[str]] = mapped_column(String(64))
     May_BD: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_June_BD: Mapped[Optional[str]] = mapped_column(String(64))
     June_BD: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_July_BD: Mapped[Optional[str]] = mapped_column(String(64))
     July_BD: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_August_BD: Mapped[Optional[str]] = mapped_column(String(64))
     August_BD: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_September_BD: Mapped[Optional[str]] = mapped_column(String(64))
     September_BD: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_October_BD: Mapped[Optional[str]] = mapped_column(String(64))
     October_BD: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_November_BD: Mapped[Optional[str]] = mapped_column(String(64))
     November_BD: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_December_BD: Mapped[Optional[str]] = mapped_column(String(64))
     December_BD: Mapped[datetime] = mapped_column(DateTime)

     class SalesFigure(BaseModel, Base):
      __tablename__ = "sales_figure"
     id: Mapped[int] = mapped_column(Integer, primary_key=True)
     created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
     updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
     created_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
     updated_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
     unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
     Balance_For_January_sales: Mapped[Optional[str]] = mapped_column(String(64))
     January_sales: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_Feburary_sales: Mapped[Optional[str]] = mapped_column(String(64))
     Feburary_sales: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_March_sales: Mapped[Optional[str]] = mapped_column(String(64))
     March_sales: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_April_sales: Mapped[Optional[str]] = mapped_column(String(64))
     April_sales: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_May_sales: Mapped[Optional[str]] = mapped_column(String(64))
     May_sales: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_June_sales: Mapped[Optional[str]] = mapped_column(String(64))
     June_sales: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_July_sales: Mapped[Optional[str]] = mapped_column(String(64))
     July_sales: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_August_sales: Mapped[Optional[str]] = mapped_column(String(64))
     August_sales: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_September_sales: Mapped[Optional[str]] = mapped_column(String(64))
     September_sales: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_October_sales: Mapped[Optional[str]] = mapped_column(String(64))
     October_sales: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_November_sales: Mapped[Optional[str]] = mapped_column(String(64))
     November_sales: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_December_sales: Mapped[Optional[str]] = mapped_column(String(64))
     December_sales: Mapped[datetime] = mapped_column(DateTime)

     class InventoryLevels(BaseModel, Base):
      __tablename__ = "inventory_levels"
     id: Mapped[int] = mapped_column(Integer, primary_key=True)
     created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
     updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
     created_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
     updated_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
     unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
     Balance_For_January_inventory: Mapped[Optional[str]] = mapped_column(String(64))
     January_inventory: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_Feburary_inventory: Mapped[Optional[str]] = mapped_column(String(64))
     Feburary_inventory: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_March_inventory: Mapped[Optional[str]] = mapped_column(String(64))
     March_inventory: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_April_inventory: Mapped[Optional[str]] = mapped_column(String(64))
     April_inventory: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_May_inventory: Mapped[Optional[str]] = mapped_column(String(64))
     May_inventory: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_June_inventory: Mapped[Optional[str]] = mapped_column(String(64))
     June_inventory: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_July_inventory: Mapped[Optional[str]] = mapped_column(String(64))
     July_inventory: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_August_inventory: Mapped[Optional[str]] = mapped_column(String(64))
     August_inventory: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_September_inventory: Mapped[Optional[str]] = mapped_column(String(64))
     September_inventory: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_October_inventory: Mapped[Optional[str]] = mapped_column(String(64))
     October_inventory: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_November_inventory: Mapped[Optional[str]] = mapped_column(String(64))
     November_inventory: Mapped[datetime] = mapped_column(DateTime)
     Balance_For_December_inventory: Mapped[Optional[str]] = mapped_column(String(64))
     December_inventory: Mapped[datetime] = mapped_column(DateTime)
    

















   


