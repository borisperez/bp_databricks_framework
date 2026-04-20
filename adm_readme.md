# Run your pipeline on Databricks
You'll have to repeat the following commands whenever you updated any files. These commands help you run your pipeline on Databricks using your own Databricks Cluster in Dev workspaces. 
## Deploy Asset bundle to Databricks
  `databricks bundle deploy -t dev`
## Run your pipeline as workflow on Databricks
  `databricks bundle run -t dev <your_workflow_name_under_folder_workflows>`
# Update table schema
Run the command below to update table schema if you've updated any data contract file.

```databricks bundle deploy -t dev```

```databricks bundle run -t dev bundle_<your_project_name>_update_table_schema```

Wait until seeing the log message from Databricks in your terminal