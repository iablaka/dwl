# As a User, I Can Create a New Right

* Version: **0.0.1**
* Creation Date: **Aug 11, 2023**
* Last Update: **Aug 11, 2023**
* Status: **DONE**

## Description

A user can create a new permission querying the POST /iam/rights route and providing a body with its name

## Acceptance Crtieria
*Given* I am a user no matter what my authroizations are

*When* I call the POST /iam/rights route with the below body

*Then* a right with the given name is added to the database if it was not already existing

{
    "name": "module:feature:verb"
}


