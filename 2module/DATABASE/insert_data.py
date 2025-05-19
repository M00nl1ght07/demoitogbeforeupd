import pandas as pd
import psycopg

from config import *

def insert_suppliers(conn):
    df = pd.read_excel(
        "1module/EXCEL/Suppliers_import.xlsx",
        engine="openpyxl"
    )
    query = """
    insert into suppliers
    values (%s, %s, %s, %s, %s)
    """


    for row in df.itertuples():
        values = (
            row._1,
            row._2,
            row.ИНН,
            row.Рейтинг,
            pd.to_datetime(row._5).date())
        cursor = conn.cursor()
        cursor.execute(query, values)
    
    conn.commit()

def insert_products(conn):
    df = pd.read_excel(
        "1module/EXCEL/Product_type_import.xlsx",
        engine="openpyxl"
    )
    query = """
        insert into products_type
        values (%s, %s)
        """

    for row in df.itertuples():
        values = (

            row._1,
            row._2
        )

        cursor = conn.cursor()
        cursor.execute(query, values)

    conn.commit()


def insert_materials_type(conn):
    df = pd.read_excel(
        "1module/EXCEL/Material_type_import.xlsx",
        engine="openpyxl"
    )
    query = """
        insert into materials_type
        values (%s, %s)
        """

    for row in df.itertuples():
        values = (

            row._1,
            f"{round(float(row._2)*100, 2)}%"
        )
        print(values)

        cursor = conn.cursor()
        cursor.execute(query, values)

    conn.commit()

def insert_materials(conn):
    df = pd.read_excel(
        "1module/EXCEL/Materials_import.xlsx",
        engine="openpyxl"
    )
    query = """
         insert into materials
         values (%s, %s, %s, %s, %s, %s, %s)
         """

    for row in df.itertuples():
        print(row)
        values = (
            row._1,
            row._2,
            round(row._3, 2),
            row._4,
            row._5,
            row._6,
            row._7

        )
        cursor = conn.cursor()
        cursor.execute(query, values)
    
    conn.commit()

def insert_materials_suppliers(conn):
    df = pd.read_excel(
        "1module/EXCEL/Material_suppliers_import.xlsx",
        engine="openpyxl"
    )
    query = """
             insert into material_suppliers
             values (%s, %s)
             """

    for row in df.itertuples():
        print(row)
        values = (
            row._1,
            row.Поставщик

        )

        cursor = conn.cursor()
        cursor.execute(query, values)

    conn.commit()


conn = psycopg.connect(
    user=USER,
    host=HOST,
    password=PASSWORD,
    dbname=DBNAME
)


insert_suppliers(conn)
insert_products(conn)
insert_materials_type(conn)
insert_materials(conn)
insert_materials_suppliers(conn)