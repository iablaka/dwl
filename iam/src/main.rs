use diesel::pg::PgConnection;
use diesel::prelude::*;
use dotenvy::dotenv;
use std::env;
use actix_web::{get, web, App, HttpServer, Responder, HttpResponse};
use uuid::Uuid;

mod models;
mod schema;

fn establish_connection() -> PgConnection {
    dotenv().ok();
    let database_url = env::var("DATABASE_URL").expect("DATABASE_URL must be set");
    PgConnection::establish(&database_url)
        .unwrap_or_else(|_| panic!("Error connecting to {}", database_url))
}


#[get("/")]
async fn health() -> impl Responder {
    HttpResponse::Ok().body("Server is alive and responds")
}

#[get("/iam/account/{account_id}")]
async fn get_account(account_id: web::Path<String>) -> impl Responder {
    
    use schema::account::dsl::*;
    
    let account_id = account_id.into_inner();
    let connection = &mut establish_connection();
    let result = account
        .filter(name.eq(account_id))
        .limit(1)
        .load::<models::Account>(connection)
        .expect("Error loading accounts");
    HttpResponse::Ok().body(result.len().to_string())
}


#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(health)
            .service(get_account)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}