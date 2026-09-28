# Big Data Interoperability Pipeline

A high-performance PySpark data processing pipeline designed to read heterogeneous big data storage formats (**Apache Avro**, **JSON**, and **Apache Parquet**) from **HDFS** and convert them into **Snappy-compressed CSV** files.

This project demonstrates cross-format big data interoperability, handling complex structured/semi-structured/unstructured data schemas, top-level array flattening, and HDFS integration.

---

## 🏗️ Architecture & Technology Stack

* **Processing Engine:** Apache Spark (PySpark 3.x)
* **Distributed Storage:** Apache Hadoop HDFS (`hdfs://localhost:9000`)
* **Environment:** Linux (CentOS / RHEL / Ubuntu)
* **Input Formats:** Apache Avro (`.avro`), JSON (`.json`), Apache Parquet (`.parquet`)
* **Output Format:** CSV (`.csv`) with Snappy compression (`.snappy`)

---

## 📂 Project Structure

```text
BigData_Interoperability_Pipeline/
│
├── avro.py         # PySpark job for Avro format processing
├── jsonpro.py      # PySpark job for multi-line JSON & structural array flattening
├── parquet.py      # PySpark job for Parquet format processing
└── README.md       # Project documentation
