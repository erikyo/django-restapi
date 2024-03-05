CREATE TABLE categories (
    id serial PRIMARY KEY,
    name VARCHAR (255) UNIQUE,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id serial PRIMARY KEY,
    name VARCHAR (255),
    category_id INTEGER REFERENCES categories(id),
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);