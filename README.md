## ETL-Pipeline-from-Azure-SQL-to-Azure Blob-using-Azure-Databricks

This projects walks you through an ETL pipeline which copy data from Azure SQL database to Azure data lake storage gen2 using Azure Databricks. Azure Databricks handles all the transformation and cleaning process and finally loads the processed data to the destination data store.

### This project involves creating three reources:
- Azure Databricks.
- Azure blob storage.
- Azure SQL database.

### This project performs the following operations:
1. Extract data from Azure SQL tables
2. Transform the data with business rules using Azure Databricks
3. Load the data to Azure blob storage

### Cleaning operations:
1. Update Outlet_Size = Small where it is null.
2. Update Outletwt_Location = Tier1 where its null.
3. Update Item_Fat_Content_LF to Low Fat.

### Create resources needed for the project.
![Create resources needed for the project](https://github.com/Nkamanyi/ETL-Pipeline-from-Azure-SQL-to-Azure-Blob-using-Azure-Databricks/blob/main/Create%20resources%20needed%20for%20the%20project.png)

### Create a sample database.
![Create a sample database](https://github.com/Nkamanyi/ETL-Pipeline-from-Azure-SQL-to-Azure-Blob-using-Azure-Databricks/blob/main/Create%20a%20sample%20database.png)

![Create container to store incoming data](https://github.com/Nkamanyi/ETL-Pipeline-from-Azure-SQL-to-Azure-Blob-using-Azure-Databricks/blob/main/A%20little%20query%20on%20the%20sample%20database%20to%20confirm%20its%20creation.png)

### Create container to store incoming data.
![Create container to store incoming data](https://github.com/Nkamanyi/ETL-Pipeline-from-Azure-SQL-to-Azure-Blob-using-Azure-Databricks/blob/main/Create%20container%20to%20store%20incoming%20data.png)

### Azure Databricks processing.
![Azure Databricks processing](https://github.com/Nkamanyi/ETL-Pipeline-from-Azure-SQL-to-Azure-Blob-using-Azure-Databricks/blob/main/Azure%20Databricks%20processing.png)

### Processed data in Azure blob storage.
![Processed data in Azure blob storage](https://github.com/Nkamanyi/ETL-Pipeline-from-Azure-SQL-to-Azure-Blob-using-Azure-Databricks/blob/main/Processed%20data%20in%20Azure%20blob%20storage.png)
