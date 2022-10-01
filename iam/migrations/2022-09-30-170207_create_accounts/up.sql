-- Create Account table
CREATE TABLE account (
  id UUID PRIMARY KEY,
  name VARCHAR NOT NULL,
  parent_id UUID NULL
)