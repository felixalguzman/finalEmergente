![Screenshot from 2019-07-26 22-40-58](https://user-images.githubusercontent.com/17243615/151471385-2dd37ed5-19a3-4935-bed1-8a399a4341ff.png)



# ANÁLISIS VENTAS UTILIZANDO MAPREDUCE SOBRE CLUSTER HADOOP

1. Desarrollar un script, en cualquier lenguaje de programación, que genere un DataSet
con al menos 1000 registros de Ventas por mes de Cada Sucursal que posee la empresa
ABC. Este dataset debe tener la siguiente estructura:

| Ciudad        | Mes           | MontoVenta  |
| ------------- |-------------| ----- |
| Santiago    | Enero | 1000.00 | 
| La Vega     | Enero      |   1500.00 |
| Santiago | Febrero      |    3000.00 |
| Moca    | Enero | 2500.00 |
| La Vega | Abril | 3500.00 |


2. Luego utilizando el DataSet generado por ustedes en el punto anterior, desarrollar
Mappers and Reducers que se encarguen de determinar los siguientes datos:
* Total Ventas x Cada Ciudad
* Total Ventas x Cada Mes
* Mes con Mayor Venta
* Ciudad con Mayor Venta
* Mostrar el Total Ventas para los Meses Enero y Marzo en la Ciudades de Santiago, La Vega y Moca.

3. Archivos a entregar:
* El código de cada Mapper*.py y Reducer*.py, desarrollado para obtener los datos.
* Archivo DataSet.
* Documento PDF, con los pasos que llevaron acabo para hacer el análisis de los
datos. Es decir, desde la generación del DataSet hasta la ejecución de los
MapReduce en el Cluster Hadoop.

4. Información a tomar en cuenta:
* Si esta tarea la realiza utilizando Apache Spark y su nota final está por debajo de 79.50 tiene derecho a un Bono para pasar a la próxima letra. Es decir si su nota final es 65 y entró la tarea con Spark, tiene una C.
* Si su nota final está entre 83 y 89 y nunca ha fallado entrengando tarea, siempre ha participado en la clase y entrega la tarea final utilizando Apache Spark, entonces tiene derecho a una A.

5. Los Criterios de evaluación son:
* El primer Punto tiene un valor de 4 Puntos.
* Las consultas a y b tienen un valor de 2 puntos.
* Las consulta c y d tienen un valor de 2.5 puntos.
* La consulta e tiene un valor de 3 puntos.
* Documento con los pasos realizados 3 puntos
