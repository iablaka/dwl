use diesel::prelude::*;
use uuid::Uuid;

#[derive(Queryable)]
pub struct Account {
    pub id: Uuid,
    pub name: String,
    pub parent_id: Option<Uuid>,
}