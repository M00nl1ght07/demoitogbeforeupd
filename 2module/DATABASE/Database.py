from DATABASE.config import *
import psycopg

class Database:

    def __init__(self):
        self.connection = self.connect_to_db()

    def connect_to_db(self):
        try:
            conn = psycopg.connect(
                user=USER,
                host=HOST,
                password=PASSWORD,
                dbname=DBNAME
            )
            return conn

        except Exception as e:
            print(e)
            return None

    def take_materials_data(self):
        """
        Получение данных о всех материалах
        :return: list
        """

        try:
            query = """
            select *
            from materials;"""
            cursor = self.connection.cursor()
            cursor.execute(query)

            result = []
            for row in cursor.fetchall():
                result.append(
                    {
                        'name':row[0],
                        'type':row[1],
                        'cost':row[2],
                        'count':row[3],
                        'min_count':row[4],
                        'size':row[5],
                        'edinica':row[6]
                    }
                )

            return result

        except Exception as e:
            print(e)
            return []
