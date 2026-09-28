from pyspark.sql import SparkSession
from pyspark.sql.functions import explode

spark = SparkSession.builder.appName("jsonproject").getOrCreate()

json_df = spark.read.format("json") \
    .option("multiLine", "true") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("hdfs://localhost:9000/unstructure/airports.json")

flat_df = json_df.select(explode("airports").alias("airport")).select("airport.*")

flat_df.show()

flat_df.write.format("csv") \
    .mode("overwrite") \
    .option("compression", "snappy") \
    .save("hdfs://localhost:9000/unstructure/df_json")

spark.stop()
