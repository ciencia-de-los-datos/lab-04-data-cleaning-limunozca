


import pandas as pd

def clean_data():

    #
    # Inserte su código aquí

    #return df

#Normalizar la data

    df_data = clean_data()

df_data = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
df_data.dropna(inplace=True)  #eliminamos valores NaN

#aplico funcion lambada para convertir todas las columnas a texto
df_data = df_data.apply(lambda x: x.astype(str))

#convierto todas las columnas a minusculas
df_data = df_data.apply(lambda x: x.str.lower())

#Normalizo los carécteres especiales    
df_data = df_data.apply(lambda x: x.str.replace(",", ""))
df_data = df_data.apply(lambda x: x.str.replace("_", "-"))
df_data = df_data.apply(lambda x: x.str.replace("-", " "))
df_data = df_data.apply(lambda x: x.str.replace("$", ""))


#Normalizo el monto del crédito a tipo float
df_data.monto_del_credito = df_data.monto_del_credito.astype(float)

# convierto fecha a formano YYYY-MM-DD
df_data.fecha_de_beneficio = pd.to_datetime(df_data["fecha_de_beneficio"], dayfirst=True, format="mixed")

#Reviso de nuevo duplicados
df_data.drop_duplicates(inplace=True)

def clean_data():
    return df_data
#print(clean_data())


# # def sexo():
# #     df_data = clean_data()
# #     return df_data.sexo.value_counts().tolist()
# # print(conteo_sexo())

# def tipo_de_emprendimiento():
#     df_data = clean_data()
#     return df_data.tipo_de_emprendimiento.value_counts().tolist()
# print(tipo_de_emprendimiento())



























# """
# Limpieza de datos usando Pandas
# -----------------------------------------------------------------------------------------

# Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
# correctamente. Tenga en cuenta datos faltantes y duplicados.

# """
# import pandas as pd

# def clean_data():
#     """
#     Limpieza de datos
#     """
# df_data = clean_data()

# df_data = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
# df_data.dropna(inplace=True)
# #df_data.drop_duplicates(inplace=True)


# #convertir a texto todas las columnas
# df_data = df_data.apply(lambda x: x.astype(str))

# #convertir en minúculas todas las columnas
# df_data = df_data.apply(lambda x: x.str.lower())
# #Limpieza de caracteres especiales. 
# df_data = df_data.apply(lambda x: x.str.replace("-", " "))
# df_data = df_data.apply(lambda x: x.str.replace(",", ""))
# df_data = df_data.apply(lambda x: x.str.replace("_", "-"))
# df_data = df_data.apply(lambda x: x.str.replace("$", ""))

# #normalizar el formato de fecha a YYYY-MM-DD
# df_data.fecha_de_beneficio = pd.to_datetime(df_data["fecha_de_beneficio"], dayfirst=True, format="mixed")
# #df_data["fecha_de_beneficio"] = pd.to_datetime(df_data["fecha_de_beneficio"], format="%d/%m/%Y", errors='coerce').dt.strftime('%Y-%m-%d')

# #normalizar monto del crédito
# df_data.monto_del_credito = df_data.monto_del_credito.astype(float)

# #Duplicados
# df_data.drop_duplicates(inplace=True)

# def clean_data():
#     return df_data
# def get_sexo_counts():
#      df = clean_data()
#      sexo_counts = df["sexo"].value_counts().tolist()
#      return sexo_counts
#  #print(get_sexo_counts())
# print(clean_data())
 
