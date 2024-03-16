# Databricks notebook source
# MAGIC %md
# MAGIC ### Acessando o Azure Data Lake, usando Blob Access Key
# MAGIC 1. Introduzir o fs.azure.account.key
# MAGIC 2. listar arquivos do blob storage
# MAGIC 3. ler arquivo csv

# COMMAND ----------

containerNameBronze = "raw"
storageAccountName = "stgf1databricksms"
blobAcessKey = "WmwyR2hU3DD5icwiqFrbyIEJLKj7sqLA0+NRnhA6hycA2yyZ3DAjJGlUXxrm1ywamXDJ1fTCbbKT+AStYnzk1Q=="

dbutils.fs.mount(
source = "wasbs://" + containerNameBronze + "@" + storageAccountName + ".blob.core.windows.net",
  mount_point = "/mnt/raw",
  extra_configs = {"fs.azure.account.key." + storageAccountName + ".blob.core.windows.net":blobAcessKey })


# COMMAND ----------

containerNameSilver = "silver"
storageAccountName = "stgf1databricksms"
blobAcessKey = "WmwyR2hU3DD5icwiqFrbyIEJLKj7sqLA0+NRnhA6hycA2yyZ3DAjJGlUXxrm1ywamXDJ1fTCbbKT+AStYnzk1Q=="

dbutils.fs.mount(
source = "wasbs://" + containerNameSilver + "@" + storageAccountName + ".blob.core.windows.net",
  mount_point = "/mnt/silver",
  extra_configs = {"fs.azure.account.key." + storageAccountName + ".blob.core.windows.net":blobAcessKey })

# COMMAND ----------

containerNameGold = "gold"
storageAccountName = "stgf1databricksms"
blobAcessKey = "WmwyR2hU3DD5icwiqFrbyIEJLKj7sqLA0+NRnhA6hycA2yyZ3DAjJGlUXxrm1ywamXDJ1fTCbbKT+AStYnzk1Q=="

dbutils.fs.mount(
source = "wasbs://" + containerNameGold + "@" + storageAccountName + ".blob.core.windows.net",
  mount_point = "/mnt/gold",
  extra_configs = {"fs.azure.account.key." + storageAccountName + ".blob.core.windows.net":blobAcessKey })
