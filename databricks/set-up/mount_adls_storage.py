# Databricks notebook source
storage_account_name = "formulaumstg"
client_id            = dbutils.secrets.get(scope="formula1-scope", key="formula1-app-client")
tenant_id            = dbutils.secrets.get(scope="formula1-scope", key="formula1-app-tenant")
client_secret        = dbutils.secrets.get(scope="formula1-scope", key="formula1-app-client-secret")

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{client_id}",
           "fs.azure.account.oauth2.client.secret": f"{client_secret}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

# COMMAND ----------

def mount_adls(container_name):
  dbutils.fs.mount(
    source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storage_account_name}/{container_name}",
    extra_configs = configs)

# COMMAND ----------

mount_adls("bronze")

# COMMAND ----------

mount_adls("silver")

# COMMAND ----------

mount_adls("gold")

# COMMAND ----------

mount_adls("demo")

# COMMAND ----------

dbutils.fs.ls("/mnt")

# COMMAND ----------

dbutils.fs.ls("/mnt/formulaumstg/bronze")

# COMMAND ----------

dbutils.fs.ls("/mnt/formulaumstg/silver")

# COMMAND ----------

dbutils.fs.ls("/mnt/formulaumstg/gold")

# COMMAND ----------

dbutils.fs.ls("/mnt/formulaumstg/demo")

# COMMAND ----------

