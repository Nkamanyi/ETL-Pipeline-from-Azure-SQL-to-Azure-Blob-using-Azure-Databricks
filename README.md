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
