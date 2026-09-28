from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("parquetproject").getOrCreate()

par = spark.read.format("parquet") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("hdfs://localhost:9000/semistructure/parquet.parquet")

par.show()

par.write.format("csv") \
    .mode("overwrite") \
    .option("compression", "snappy") \
    .save("hdfs://localhost:9000/semistructure/df_par")

spark.stop()
