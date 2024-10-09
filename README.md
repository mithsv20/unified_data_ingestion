
---
# 📊 PySpark ETL Framework unified_data_ingestion


Welcome to the PySpark ETL Framework unified_data_ingestion! This repository helps you easily read, transform, and write data using PySpark. Whether you're working with CSV, JSON, or other data formats, this framework is designed to make your life easier. Let’s dive in! 🚀

## 📁 Getting Started

### 🛠️ Prerequisites

Before you begin, make sure you have:

- Python installed (version 3.6 or higher) 🐍
- Apache Spark installed (with PySpark) 🌟
- Required Python packages (see `requirements.txt`) 📦

### 📂 Repository Structure

Here’s what you’ll find in this repository:

```
pyspark_framework/
│
├── config/                   # Contains configuration files
│   └── config.json           # JSON file with read, transform, and write settings
│
├── src/                      # Contains all the source code
│   ├── main.py               # Main execution file
│   ├── spark_utils.py        # Utility functions for Spark
│   ├── json_parser.py        # Load JSON configurations
│   ├── reads.py              # Functions to read data
│   ├── transformations.py     # Functions for data transformations
│   └── writes.py             # Functions to write data
│
└── requirements.txt          # List of dependencies
```

## 📥 Providing Input Data

1. **Prepare Your Data Files**: Place your input files (e.g., CSV, JSON) in the `data/` directory. 

2. **Configure the JSON File**: Modify the `config/config.json` file to specify your data sources. Here’s a very basic structure you can follow:

```json
{
    "spark": {
        "app_name": "AppExecution",
        "master": "local[*]"
    },
    "reads": [
        {
            "view_name": "your_view_name",
            "format": "csv",  // or "json" or "other formats"
            "path": "data/your_input_file.csv",  // specify your input file here
            "options": {
                "header": "true",
                "inferSchema": "true"
            }
        }
    ],
    "transformations": [
        {
            "query": "SELECT * FROM your_view_name",
            "view_name": "transformed_view_name"
        }
    ],
    "writes": [
        {
            "view_name": "transformed_view_name",
            "format": "csv",
            "path": "data/output_data.csv",  // specify your output file here
            "mode": "overwrite"
        }
    ]
}
```

### 🔍 Retrieving Input and Output Files

- **Input Files**: Ensure your files are correctly named and placed in the `data/` directory. You can add multiple files as needed by specifying each in the `reads` section of the JSON configuration.

- **Output Files**: After running the framework, the output files will be saved in the same `data/` directory as specified in the `writes` section of the JSON. For example, if you specify `"path": "data/output_data.csv"`, you can find your output file there.

## ⚙️ How It Works

### 📈 Transform Your Data

This framework allows you to perform multiple transformations on your data:

- Filter, join, and manipulate data using SQL queries.
- Specify temporary view names for each transformation to avoid conflicts.

### 📤 Output Data

The final output will be saved based on your configuration. Ensure you specify the correct file format and path in the `writes` section to save your processed data.

## 🌟 Key Features

- **Dynamic Multiple Reads**: Read from various formats (CSV, JSON, etc.) and create temporary views for each dataset! 🎉
- **Flexible Transformations**: Perform complex SQL transformations with ease! 🔄
- **Multiple Writes**: Save your final output in different formats and locations! 💾

## 🚧 Upcoming Enhancements

We’re continually improving this framework! Here are some planned features:

- **Custom UDF Registration**: Allow users to define and register their own User Defined Functions (UDFs) for complex transformations! 🛠️
- **Better Error Handling**: Improve error messages for easier debugging. ❌
- **User Interface**: Consider a simple UI for easier configuration. 🖥️

## 🤝 Contribution

We welcome contributions! If you have ideas or improvements, feel free to create a pull request or open an issue.

---

Happy coding! If you have any questions, feel free to reach out! 😊