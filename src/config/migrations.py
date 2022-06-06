def get():
    query = '''
        pragma foreign_keys=1;
        
        CREATE TABLE IF NOT EXISTS waste_types
        (
            id   INTEGER PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS bin_types
        (
            id            INTEGER PRIMARY KEY,
            waste_type_id INTEGER NOT NULL,
            volume        INTEGER NOT NULL,
        
            UNIQUE (waste_type_id, volume) ON CONFLICT REPLACE,
            FOREIGN KEY (waste_type_id) REFERENCES waste_types (id)
        );
        
        CREATE TABLE IF NOT EXISTS cities
        (
            id       INTEGER PRIMARY KEY,
        
            postcode VARCHAR(10) NOT NULL,
            name     VARCHAR(50) NOT NULL,
        
            UNIQUE (postcode, name) ON CONFLICT REPLACE
        );
        
        CREATE TABLE IF NOT EXISTS streets
        (
            id   INTEGER PRIMARY KEY,
        
            name VARCHAR(255) UNIQUE NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS addresses
        (
            id        INTEGER PRIMARY KEY,
        
            street_id INTEGER NOT NULL,
            city_id   INTEGER NOT NULL,
            number    INTEGER NOT NULL,
        
            FOREIGN KEY (street_id) REFERENCES streets (id),
            FOREIGN KEY (city_id) REFERENCES cities (id),
        
            UNIQUE (street_id, city_id, number) ON CONFLICT REPLACE
        );
        
        CREATE TABLE IF NOT EXISTS objects
        (
            id              INTEGER PRIMARY KEY,
            number          VARCHAR(50) UNIQUE NOT NULL,
        
            customer_number INTEGER            NOT NULL,
        
            address_id      INTEGER            NOT NULL,
        
            FOREIGN KEY (address_id) REFERENCES addresses (id)
        );
        
        CREATE TABLE IF NOT EXISTS bins
        (
            id          INTEGER PRIMARY KEY,
        
            object_id   INTEGER NOT NULL,
            bin_type_id INTEGER NOT NULL,
        
            FOREIGN KEY (object_id) REFERENCES objects (id),
            FOREIGN KEY (bin_type_id) REFERENCES bin_types (id)
        );
    '''

    return {
        "queries": query
    }
