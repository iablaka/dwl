# As a User, I Can Read the List of All Rights 

* Version: **0.0.1**
* Creation Date: **Aug 11, 2023**
* Last Update: **Aug 11, 2023**
* Status: **DONE**

## Description

A user can read the list of all existing permissions querying the GET /iam/rights route.

## Acceptance Crtieria
*Given* I am a user no matter what my authroizations are

*When* I call the GET /iam/rights route

*Then* I get the list of all existing rights from the database in the form of a json object

{
    "rights": [
        "mod0:fea0:read",
        "mod0:fea0:write",
        "mod0:fea1:read",
        "mod0:fea1:write"
    ]
}


