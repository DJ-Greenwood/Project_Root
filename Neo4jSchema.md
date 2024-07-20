// Create constraints to ensure uniqueness
CREATE CONSTRAINT FOR (ds:DataSource) REQUIRE ds.id IS UNIQUE;
CREATE CONSTRAINT FOR (etl:ETLProcess) REQUIRE etl.id IS UNIQUE;
CREATE CONSTRAINT FOR (model:MLModel) REQUIRE model.id IS UNIQUE;
CREATE CONSTRAINT FOR (output:Output) REQUIRE output.id IS UNIQUE;

// Create indexes for better performance
CREATE INDEX :DataSource(name);
CREATE INDEX FOR ETLProcess(name);
CREATE INDEX FOR MLModel(name);
CREATE INDEX FOR Output(type);

// Sample data creation
CREATE (ds:DataSource {id: "ds1", name: "Customer Data", type: "CSV", path: "/data/customers.csv"})
CREATE (etl:ETLProcess {id: "etl1", name: "Customer Data Cleaning", description: "Removes duplicates and standardizes formats"})
CREATE (model:MLModel {id: "model1", name: "Customer Churn Predictor", algorithm: "Random Forest", version: "1.0"})
CREATE (output:Output {id: "out1", type: "Prediction", description: "Churn probability for each customer"})

// Create relationships
CREATE (ds)-[:PROCESSED_BY]->(etl)
CREATE (etl)-[:FEEDS_INTO]->(model)
CREATE (model)-[:PRODUCES]->(output)

// Helper function to create a complete lineage path
CREATE PROCEDURE create_lineage_path(
  dsId: STRING, 
  dsName: STRING, 
  etlId: STRING, 
  etlName: STRING, 
  modelId: STRING, 
  modelName: STRING, 
  outputId: STRING, 
  outputType: STRING
) AS
BEGIN
  MERGE (ds:DataSource {id: dsId}) ON CREATE SET ds.name = dsName
  MERGE (etl:ETLProcess {id: etlId}) ON CREATE SET etl.name = etlName
  MERGE (model:MLModel {id: modelId}) ON CREATE SET model.name = modelName
  MERGE (output:Output {id: outputId}) ON CREATE SET output.type = outputType
  MERGE (ds)-[:PROCESSED_BY]->(etl)
  MERGE (etl)-[:FEEDS_INTO]->(model)
  MERGE (model)-[:PRODUCES]->(output)
END;

// Example usage of the helper function
CALL create_lineage_path(
  "ds2", "Sales Data", 
  "etl2", "Sales Data Aggregation", 
  "model2", "Revenue Forecasting Model", 
  "out2", "Forecast"
);