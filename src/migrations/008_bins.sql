CREATE TABLE IF NOT EXISTS bins (
    id INTEGER PRIMARY KEY,

    object_id INTEGER NOT NULL,
    bin_type_id INTEGER NOT NULL,

    FOREIGN KEY (object_id) REFERENCES objects(id),
    FOREIGN KEY (bin_type_id) REFERENCES bin_types(id)
);
