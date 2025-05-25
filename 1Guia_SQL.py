#%% Ejercicio 1: crear tabla departamentos 

#%% listar nombres de depto dejando a los repetidos 
consultaSQL = """
SELECT departamento_nombre 
FROM dengue;
"""
consulta_nombresdeptoCONREPE = db.sql(consultaSQL).df()
print(consulta_nombresdeptoCONREPE)

#%% lo mismo, pero sacando a los repetidos 

consultaSQL = """
SELECT DISTINCT departamento_nombre 
FROM dengue;
"""
consulta_nombresdeptoSINREPE = db.sql(consultaSQL).df()
print(consulta_nombresdeptoSINREPE)

#%% listar nombre e id de depto 

consultaSQL = """
SELECT DISTINCT departamento_id AS id, departamento_nombre AS nombre
FROM dengue;
"""
consulta_nombreID = db.sql(consultaSQL).df()
print(consulta_nombreID)

#%% listar columnas en gral 

consultaSQL = """
SELECT DISTINCT departamento_id AS id, departamento_nombre AS descripcion, provincia_id AS id_provincia
FROM dengue;
"""
departamento_columnas = db.sql(consultaSQL).df()
print(departamento_columnas)

#%% listar provincia 54 

consultaSQL = """
SELECT DISTINCT id, descripcion, id_provincia
FROM departamento_columnas 
WHERE id_provincia == 54
"""

departamento54 = db.sql(consultaSQL).df()
print(departamento54)

#%% ahora provincia 22, 78 o 86

consultaSQL = """
SELECT DISTINCT id, descripcion, id_provincia
FROM departamento_columnas 
WHERE id_provincia == 22 OR id_provincia == 78 OR id_provincia == 86; 
"""

departamento22 = db.sql(consultaSQL).df()
print(departamento22)

#%% entre el 50 y 59 

consultaSQL = """
SELECT DISTINCT id, descripcion, id_provincia
FROM departamento_columnas 
WHERE id_provincia >= 50 AND id_provincia <= 59; 
"""

departamento22 = db.sql(consultaSQL).df()
print(departamento22)
