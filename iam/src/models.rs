use diesel::prelude::*;
use serde::{Deserialize, Serialize};


#[derive(Deserialize, Serialize, Queryable)]
pub struct Account {
    pub id: String,
    pub name: String,
    pub parent_id: Option<String>,
}