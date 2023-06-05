# Databricks notebook source
# MAGIC %md
# MAGIC ### etl notebook based on lab 6 of Dp-203 ###
# MAGIC ## data is mnted to databricks using the credentails of ADLS ##
# MAGIC

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
       "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
       "fs.azure.account.oauth2.client.id": "f0d0eaf6-6ff5-4cb4-b696-44d42ab13dc2",
       "fs.azure.account.oauth2.client.secret": "DgY8Q~2C3BbAVulcborclAZEnEicWfQ68MbGia4y",
       "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/1df41cf9-1d8a-4ae1-a1ba-d3966c68a31e/oauth2/token",
       "fs.azure.createRemoteFileSystemDuringInitialization": "true"}


# COMMAND ----------

dbutils.fs.mount(
source = "abfss://cont2@sto2data.dfs.core.windows.net/data2/dir1",
mount_point = "/mnt/ETLdata",
extra_configs = configs)


# COMMAND ----------

dbutils.fs.ls("/mnt")
#df1=spark.read.csv("dbfs:/mnt/<foldername>/<filename.csv>")
df1=spark.read.csv("dbfs:/mnt/ETLdata/*.csv", header = True , inferSchema= True)
display(df1)


# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *

orderSchema = StructType([
    StructField("SalesOrderNumber", StringType()),
    StructField("SalesOrderLineNumber", IntegerType()),
    StructField("OrderDate", DateType()),
    StructField("CustomerName", StringType()),
    StructField("Email", StringType()),
    StructField("Item", StringType()),
    StructField("Quantity", IntegerType()),
    StructField("UnitPrice", FloatType()),
    StructField("Tax", FloatType())
    ])

df = spark.read.load('dbfs:/mnt/ETLdata/*.csv', format='csv', schema=orderSchema)
display(df.limit(100))

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## split name to 2 columns ##
# MAGIC  * transform 1 * 
# MAGIC

# COMMAND ----------

from pyspark.sql.functions import split, col

# Create the new FirstName and LastName fields
transformed_df = df.withColumn("FirstName", split(col("CustomerName"), " ").getItem(0)).withColumn("LastName", split(col("CustomerName"), " ").getItem(1))

# Remove the CustomerName field
transformed_df = transformed_df.drop("CustomerName")

display(transformed_df.limit(5))

# COMMAND ----------

# MAGIC %md
# MAGIC # save the resulting dataframe in any accepted file format #
# MAGIC ## here we are saving in Parquet Format ##

# COMMAND ----------

transformed_df.write.mode("overwrite").parquet('/mnt/transformed_data/orders.parquet')
print ("Transformed data saved!")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Partition data
# MAGIC
# MAGIC A common way to optimize performance when dealing with large volumes of data is to partition the data files based on one or more field values. This can significant improve performance and make it easier to filter data.
# MAGIC
# MAGIC Use the following cell to derive new **Year** and **Month** fields and then save the resulting data in Parquet format, partitioned by year and month.

# COMMAND ----------

from pyspark.sql.functions import year, month, col

dated_df = transformed_df.withColumn("Year", year(col("OrderDate"))).withColumn("Month", month(col("OrderDate")))
display(dated_df.limit(5))
dated_df.write.partitionBy("Year","Month").mode("overwrite").parquet("/mnt/partitioned_data")
print ("Transformed data saved!")

# COMMAND ----------

orders_2020 = spark.read.parquet('/mnt/partitioned_data/Year=2020/Month=*')
display(orders_2020.limit(5))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Use SQL to transform data
# MAGIC
# MAGIC Spark is a very flexible platform, and the **SQL** library that provides the dataframe also enables you to work with data using SQL semantics. You can query and transform data in dataframes by using SQL queries, and persist the results as tables - which are metadata abstractions over files.
# MAGIC
# MAGIC First, use the following code to save the original sales orders data (loaded from CSV files) as a table. Technically, this is an *external* table because the **path** parameter is used to specify where the data files for the table are stored (an *internal* table is stored in the system storage for the Spark metastore and managed automatically).

# COMMAND ----------

df.write.saveAsTable('sales_orders', format='parquet', mode='overwrite', path='/sales_orders_table')

# COMMAND ----------

sql_transform = spark.sql("SELECT *, YEAR(OrderDate) AS Year, MONTH(OrderDate) AS Month FROM sales_orders")
display(sql_transform.limit(5))
sql_transform.write.partitionBy("Year","Month").saveAsTable('transformed_orders', format='parquet', mode='overwrite', path='/transformed_orders_table')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM transformed_orders
# MAGIC WHERE Year = 2021
# MAGIC     AND Month = 1

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DROP TABLE transformed_orders;
# MAGIC DROP TABLE sales_orders;

# COMMAND ----------


