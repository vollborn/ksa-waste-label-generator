CREATE TABLE IF NOT EXISTS bin_types (

    id INTEGER PRIMARY KEY,
    waste_type_id INTEGER NOT NULL,
    volume INTEGER NOT NULL,

    UNIQUE (waste_type_id, volume) ON CONFLICT REPLACE,
    FOREIGN KEY (waste_type_id) REFERENCES waste_types(id)
);
