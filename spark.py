from __future__ import print_function

import sys
from random import random
from operator import add

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, Row
from pyspark.sql.types import DoubleType, IntegerType, StringType

if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    spark = SparkSession \
        .builder \
        .appName("PythonPi") \
        .getOrCreate()
    schema = StructType([
        StructField("Ciudad", StringType()),
        StructField("Mes", StringType()),
        StructField("MontoVenta", IntegerType())
    ])

    sc = spark.sparkContext
    textFile = sc.textFile("hdfs://localhost:9000/dataset.txt")
    partes = textFile.map(lambda l: l.split("\t"))
    data = partes.map(lambda p: Row(ciudad=p[0],mes=p[1],monto=int(p[2])))
    # data = partes.map(lambda p: Row(ciudad=p[0], mes=p[1], monto=int(p[2].strip())))
    df = spark.createDataFrame(data)

    df.printSchema()
    df.show()
    # ds = spark.createDataFrame(df, schema=schema)
    # ds.printSchema()
    # for line in df:
    #     print(line)

    # df.filter(df['MontoVenta'] > 5000).show()
    # df.groupBy(df['Ciudad']).sum('MontoVenta').show()
# partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2
# n = 100000 * partitions
#
# def f(_):
#     x = random() * 2 - 1
#     y = random() * 2 - 1
#     return 1 if x ** 2 + y ** 2 <= 1 else 0
#
# count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
# print("Pi is roughly %f" % (4.0 * count / n))

spark.stop()
