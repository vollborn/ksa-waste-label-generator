CREATE TABLE IF NOT EXISTS addresses (

    id INTEGER PRIMARY KEY,

    street_id INTEGER NOT NULL,
    city_id INTEGER NOT NULL,
    number INTEGER NOT NULL,

    FOREIGN KEY (street_id) REFERENCES streets(id),
    FOREIGN KEY (city_id) REFERENCES cities(id)

);
