## DWL - IAM - Data Model
See [here](../user/overall.md) for an overall description of what the project does from a functional perspective.

The iam data model is based on 5 main entities that will lead to 7 tables because of many to many relationships. The 5 main entities are:
- Account
- Group
- User
- Role
- Scope

## Account
|Field Name |Description |Example Value |Comments
--- | --- | --- | ---|
|id|a unique identifier of the account|4deee7be-d9da-493e-93d8-a1e499c677f3|
|name|text that describes the account|TBC-UK
|parent_id|the id of the parent account|49c530c7-8984-46b5-ad8d-a18a26bb8583| Not mandatory, if left blank the account is called a root account
