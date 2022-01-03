# Fichero de Configuración, en donde se especifican los parámetros del DataSet a generar y/o procesar

# Los parámetros a definir son:
# DATE1:            Fecha comienzo Dataset
# DATE2:            Fecha fin Dataset
# TIME_AGREGATION:  Expresión para definición del intervalo de tiempo base
#                   https://cloud.google.com/bigquery/docs/reference/standard-sql/timestamp_functions#timestamp_trunc
# TIME_PREFIX:      Etiqueta para referirse a lo anterior, irá en nombre del fichero
# DROP_avg_base_fee_per_gas : Si debe eliminarse esta columna (solo contendrá datos a partir del 5.Ago.2021)
# Parámetros de la Ventana Deslizante:
# INPUT_LEN:        Número de muestras de la entrada (inputs)
# OFFSET:           Muestras de offset hasta el inicio de la salida
# OUTPUT_LEN:       Número de muestras de la salida (labels)
#
# Parámetros que se definen a partir de los anteriores:
# DS_FILE:          Contendrá la ruta completa del archivo donde se almacena el DataSet

option = 2

# Ene-Nov 2021. Resolución horaria.
if option == 1: 
  DATE1 = '2021-01-01'
  DATE2 = '2021-11-30'
  TIME_AGREGATION = 'TIMESTAMP_TRUNC(timestamp, HOUR)'   
  TIME_PREFIX = 'HOUR'
  DROP_avg_base_fee_per_gas = True

# Sep-Nov 2021. Resolución 1 minuto
elif option == 2: 
  DATE1 = '2021-09-01'
  DATE2 = '2021-11-30'
  TIME_AGREGATION = 'TIMESTAMP_TRUNC(timestamp ,MINUTE)'
  TIME_PREFIX = 'MINUTE'
  DROP_avg_base_fee_per_gas = False

# Sep-Nov 2021. Resolución 5 minutos
elif option == 3:
  DATE1 = '2021-09-01'
  DATE2 = '2021-11-30'
  TIME_AGREGATION = 'TIMESTAMP_TRUNC(TIMESTAMP_SUB(timestamp, INTERVAL MOD(EXTRACT(MINUTE from timestamp), 5) MINUTE) ,MINUTE)'
  TIME_PREFIX = '5MINUTE'
  DROP_avg_base_fee_per_gas = False

# Ene 2021. Resolución 1 minuto
elif option == 4: 
  DATE1 = '2021-01-01'
  DATE2 = '2021-01-31'
  TIME_AGREGATION = 'TIMESTAMP_TRUNC(timestamp, MINUTE)'   
  TIME_PREFIX = 'MINUTE'
  DROP_avg_base_fee_per_gas = True

# Ene 2021. Resolución 5 minutos
elif option == 5:
  DATE1 = '2021-01-01'
  DATE2 = '2021-01-31'
  TIME_AGREGATION = 'TIMESTAMP_TRUNC(TIMESTAMP_SUB(timestamp, INTERVAL MOD(EXTRACT(MINUTE from timestamp), 5) MINUTE) ,MINUTE)'
  TIME_PREFIX = '5MINUTE'
  DROP_avg_base_fee_per_gas = True

else:
  print ("Error")

# Construye DS_FILE
DS_FILE = "/content/drive/MyDrive/TFM/etherdata-"+TIME_PREFIX+"-"+DATE1+"-"+DATE2+".csv"
DS_FILE_CLEAN = "/content/drive/MyDrive/TFM/etherdata-"+TIME_PREFIX+"-"+DATE1+"-"+DATE2+"-CLEAN.csv"
print ("Usando DS_FILE       : " + DS_FILE)
print ("Usando DS_FILE_CLEAN : " + DS_FILE_CLEAN)

# Autenticar en Google Cloud
# Debe existir un proyecto PROJECT con billing activado, tal como se describe en 
#   https://colab.research.google.com/notebooks/bigquery.ipynb
PROJECT    = "tfm-deepethereum"

