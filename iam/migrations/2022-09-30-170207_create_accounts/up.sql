-- Create Account table
CREATE TABLE account (
  id VARCHAR PRIMARY KEY,
  name VARCHAR NOT NULL,
  parent_id VARCHAR NULL
)