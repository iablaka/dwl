// @generated automatically by Diesel CLI.

diesel::table! {
    account (id) {
        id -> Varchar,
        name -> Varchar,
        parent_id -> Nullable<Varchar>,
    }
}
