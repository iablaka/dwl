use diesel::prelude::*;
use uuid::Uuid;
use serde::{Deserialize, de};
use serde_json;


#[derive(Deserialize, Queryable)]
pub struct Account {
    #[serde(deserialize_with = "deserialize_uuid")]
    pub id: Uuid,
    pub name: String,
    #[serde(deserialize_with = "deserialize_uuid")]
    pub parent_id: Option<Uuid>,
}

fn deserialize_uuid<'de, D>(deserializer: D) -> Result<Uuid, D::Error>
where
	D: de::Deserializer<'de>,
{
    struct JsonStringVisitor;
    impl<'de> de::Visitor<'de> for JsonStringVisitor {
        type Value = Uuid;

        fn expecting(&self, formatter: &mut std::fmt::Formatter) -> std::fmt::Result {
            formatter.write_str("a string containing json data")
        }
    
        fn visit_str<E>(self, v: &str) -> Result<Self::Value, E>
        where
            E: de::Error,
        {
            serde_json::from_str(v).map_err(E::custom)
        }
    }
    
    deserializer.deserialize_any(JsonStringVisitor)
}