from django.db import connection

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    resultado=[]
    for row in cursor.fetchall():
        resultado.append(dict(zip(columns, row)))        
    return resultado


def hacerConsultaSQL(consulta):
    with connection.cursor() as cursor:
        cursor.execute(consulta)
        result = dictfetchall(cursor)
        cursor.close()
        return result