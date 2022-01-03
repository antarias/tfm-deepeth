# tfm-deepeth
Anexos del TFM
"Estimación del Coste del Gas en transacciones de Ethereum mediante Deep Learning" 
Antonio Arias Sánchez. Sep 2021-Ene 2022

Scripts Python

Pra su correcta ejecución deben copiarse a una carpeta de Google Drive, y otorgarles permisos de acceso a la misma. Los scripts y su contenido son los siguientes:

0.config.py

Fichero de configuración incluido por los demás scripts, que define el rango de fechas, resolución horaria y nombre del Dataset a emplear.

1.Preparar Dataset.ipynb

Script que captura el Dataset según los parámetros definidos a partir de BigQuery, y lo almacena en Google Drive

2.Limpiar y Preparar.ipynb

Script que lee el Dataset anteriormente generado, lo limpia de outliers y elementos vacíos, y lo almacena de nuevo en Google Drive

3.Analisis Dataset.ipynb

Script que realiza el Análisis preliminar de datos del dataset seleccionado.

4.Entrenar y Probar.ipynb

Script que crea, entrena y compara los resultados de varios modelos con el dataset indicado.
