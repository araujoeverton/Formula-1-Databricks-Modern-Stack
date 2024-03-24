-- Databricks notebook source
-- MAGIC %md
-- MAGIC ##### Drop all the tables

-- COMMAND ----------

DROP DATABASE IF EXISTS silver CASCADE;

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS silver
LOCATION "/mnt/formulaumstg/silver";

-- COMMAND ----------

DROP DATABASE IF EXISTS gold CASCADE;

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS gold 
LOCATION "/mnt/formulaumstg/gold";

-- COMMAND ----------

