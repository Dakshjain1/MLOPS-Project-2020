# Databricks notebook source
# connect to blob storage
key = "-------------------------------------"

dbutils.fs.mount(
  source = "wasbs://mlopscontainer@mlopsprojblob.blob.core.windows.net",
  mount_point = "/mnt/blob",
  extra_configs = {"fs.azure.account.key.mlopsprojblob.blob.core.windows.net":key})

# COMMAND ----------

dbutils.fs.ls("/mnt/blob")

# COMMAND ----------

display(dbutils.fs.ls("/mnt/blob"))

# COMMAND ----------

pip install -r "/dbfs/FileStore/module/requirements.txt"


# COMMAND ----------

dbutils.fs.cp("/FileStore/module/package-0.1.0-py3.8.egg", "file:/tmp/package-0.1.0-py3.8.zip")

# COMMAND ----------

import zipfile
with zipfile.ZipFile('/tmp/package-0.1.0-py3.8.zip', 'r') as zip_ref:
    zip_ref.extractall('/tmp/wordcloudmodule/')

# COMMAND ----------

dbutils.fs.cp( "file:/tmp/wordcloudmodule/", "/FileStore/module/wordcloudmodule", True)

# COMMAND ----------

import sys
modulePath = "/dbfs/FileStore/module/wordcloudmodule/package"
sys.path.append(modulePath)
print(sys.path)

# COMMAND ----------

from review2wordcloud import *

# COMMAND ----------

p = "/dbfs/mnt/blob/reviews.txt"
txt2string(p)

# COMMAND ----------

dbutils.fs.cp( "/FileStore/plots/de5f71ed-7f0d-4ddd-b01b-7cf79d3a8710.png", "/mnt/blob", True)



# COMMAND ----------


