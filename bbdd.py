
import pymysql.cursors
connection = pymysql.connect(host='Juanmacaro.mysql.pythonanywhere-services.com',
                             user='Juanmacaro',
                             password='crnvx7PylZ',
                             database='Juanmacaro$adm_db')

def modificar_db(query):
    cursor= connection.cursor()  
    cursor.execute(query)     
    connection.commit()
    return

def consultar_db(query):
    cursor= connection.cursor()
    cursor.execute(query)
    Result= cursor.fetchall() 
    return Result       