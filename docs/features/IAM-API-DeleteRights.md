# As a User, I Can Delete an Existing Right

* Version: **0.0.1**
* Creation Date: **Aug 11, 2023**
* Last Update: **Aug 11, 2023**
* Status: **DONE**

## Description

A user can delete an existing permission querying the DELETE /iam/rights/<id> route and providing its id

## Acceptance Crtieria
### Scenario 1 ###
*Given* I am a user no matter what my authroizations are

*When* I call the DELETE /iam/rights/<id> route with an existing right id

*Then* this right is removed from the database
### Scenario 2 ###
*Given* I am a user no matter what my authroizations are

*When* I call the DELETE /iam/rights/<id> route with an unknown right id

*Then* nothing happens


