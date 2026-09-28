from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("avroproject").getOrCreate()

avro = spark.read.format("avro") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("hdfs://localhost:9000/unstructure/users.avro")

avro.show()

avro.write.format("csv") \
    .mode("overwrite") \
    .option("compression", "snappy") \
    .save("hdfs://localhost:9000/unstructure/df_avro")

spark.stop()
