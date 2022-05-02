CREATE TABLE IF NOT EXISTS objects (

    id INTEGER PRIMARY KEY,
    number VARCHAR(50) NOT NULL,

    customer_number INTEGER NOT NULL,

    address_id INTEGER NOT NULL,

    FOREIGN KEY (address_id) REFERENCES addresses(id)
);
