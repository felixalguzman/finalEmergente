from __future__ import print_function

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import Row
from pyspark.sql import functions as F

if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    spark = SparkSession \
        .builder \
        .appName("PythonPi") \
        .getOrCreate()

    sc = spark.sparkContext
    textFile = sc.textFile("hdfs://localhost:9000/dataset.txt")
    partes = textFile.map(lambda l: l.split("\t"))
    data = partes.map(lambda p: Row(ciudad=p[0], mes=p[1], monto=int(p[2])))
    df = spark.createDataFrame(data)

    df.printSchema()
    # df.show()

    print('total de ventas x ciudad')
    df.groupBy('ciudad').sum('monto').show()

    print('total de ventas x mes')
    df.groupBy('mes').sum('monto').sort('mes').show()

    print('mes con mayor venta')
    # df.orderBy(F.desc('monto')).limit(1).show()
    df.groupBy('mes').sum('monto').orderBy(col('sum(monto)').desc()).limit(1).show()

    print('ciudad con mayor venta')
    df.groupBy('ciudad').sum('monto').orderBy(col('sum(monto)').desc()).limit(1).show()

    print('Mostrar el Total Ventas para los Meses Enero y Marzo en la Ciudades de Santiago, La Vega y Moca.')
    df.filter(
        col('ciudad').eqNullSafe('Santiago de los Caballeros').__or__(col('ciudad').eqNullSafe('Moca')).__or__(col('ciudad').eqNullSafe('La vega')).__and__(col('mes').eqNullSafe('Marzo').__or__(col('mes').eqNullSafe('Enero')))
    ).groupBy('ciudad', 'mes').sum('monto').show()

    spark.stop()
