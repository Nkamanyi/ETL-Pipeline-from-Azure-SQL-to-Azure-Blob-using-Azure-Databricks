# Databricks notebook source
df = (spark.read
  .format("jdbc")
  .option("url", "jdbc:sqlserver://nkam-sqlserver.database.windows.net:1433;databaseName=nkam-")
  .option("dbtable", "outlet")
  .option("user", "******")
  .option("password", "*******")
  .load()
)

df.show()

# COMMAND ----------

display(df)

# COMMAND ----------

# DBTITLE 1,Cleaning
df = df.na.fill({'Outlet_Size':'Small'})

df.show()

display(df)

# COMMAND ----------

df = df.na.fill({'Outlet_Location_Type': 'Tier1'})

df.show()

display(df)

# COMMAND ----------

df = df.replace('LF','Low Fat','Item_Fat_Content')

df.show()

display(df)

# COMMAND ----------

dbutils.fs.mount(
  source="wasbs://processed-data@nkamblob.blob.core.windows.net",
  mount_point="/mnt/processed-data1",
  extra_configs={"fs.azure.account.key.nkamblob.blob.core.windows.net":"nhP/1psSpo0wPfL/urfohzhYDiuFrFa4Ihh0XTzDhISAsRmLCwg0zbYUjZnsVQhzPVLPXiet6evL+AStzqB9AA=="}
)


# COMMAND ----------

dbutils.fs.ls("/mnt/processed-data1")


# COMMAND ----------

df.repartition(1).write.mode('overwrite').options(header='True').csv("/mnt/processed-data1/")

# COMMAND ----------


