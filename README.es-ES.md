

# Conjunto de Datos de Distritos de Arabia Saudita

## Acerca de 

Este conjunto de datos es una colección de archivos relacionados con los distritos de Arabia Saudita. Los datos se recopilaron manualmente. Esta información incluye datos generales sobre los distritos del Reino de Arabia Saudita, como el número de residentes, la proporción de sauditas y extranjeros, la distribución por sexo (hombres y mujeres), además del ingreso promedio. Los datos se recopilaron manualmente desde [Nine Tenths](https://map.910ths.sa/).

## Créditos

[Ali Alohali](http://alioh.com), [Sara AlSiyat](http://linkedin.com/in/saraalsiyat), [Ibrahim AlHammad](http://linkedin.com/in/ibrahim-alhammad-7228b3178), [Nora AlAmri](https://www.linkedin.com/in/nora-alamri) y [Rawan AlMohimeed](https://www.linkedin.com/in/rawanmohimeed).

## Streamlit

[Ver la aplicación](https://share.streamlit.io/alioh/saudi-districts-dataset/main/main.py)

## Agradecimientos

Gracias a los siguientes colaboradores:

**Nombre**|**Contribución**
:-----:|:-----:|
[Dr. Najwa Alghmadi](https://www.najwa-alghmadi.net/)|Proporcionó la mayor parte de los datos de latitud/longitud.

## Elementos de datos

Algunas columnas se recopilaron manualmente y para otras utilizamos cálculos sencillos para obtenerlas

**Etiqueta**|**Tipo**|**Fuente (o columnas)**
:-----:|:-----:|:-----
District_name_EN|Texto|Traducido manualmente
District_name_AR|Texto|Nine Tenths
latitude|Número (Decimal)|Recopilado manualmente
longitude|Número (Decimal)|Recopilado manualmente
Population|Número|Nine Tenths
Males_(%)|Número (Decimal)|Nine Tenths
Females_(%)|Número (Decimal)|= 1 - [Males (%)]
Saudis_(%)|Número (Decimal)|Nine Tenths
Non_Saudis_(%)|Número (Decimal)|= 1 - [Saudis (%)]
Males|Número|= [Males (%)] * [Population]
Females|Número|= [Population] - [Males]
Saudis|Número|= [Saudis (%)] * [Population]
Non_Saudis|Número|= [Population] - [Saudis]
Average_Income|Número|Nine Tenths

## Nota

Algunas entradas son 0; en el caso del ingreso, significa no disponible. Si toda la fila es 0, significa que los datos no están disponibles. En otros campos significa un 0% o 0 real.

## Próximos pasos

- Agregar más ciudades.
- Agregar más datos.
    * Distribución del ingreso por edad, sexo y nacionalidad.
    * Agregar las coordenadas de los distritos como polígonos.
    * Códigos postales.
- Convertir los datos a base de datos SQL, Excel y JSON.

## Colaboración

Puedes enviar tus ideas o modificaciones a este conjunto de datos. Las revisaremos y las aprobaremos.

## Uso

Siéntete libre de utilizar el conjunto de datos **siempre que cites a los autores**.
