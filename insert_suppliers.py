import pandas as pd

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