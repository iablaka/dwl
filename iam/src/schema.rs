// @generated automatically by Diesel CLI.

diesel::table! {
    account (id) {
        id -> Uuid,
        name -> Varchar,
        parent_id -> Nullable<Uuid>,
    }
}
