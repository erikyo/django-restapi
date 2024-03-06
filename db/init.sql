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

-- Insert sample data
INSERT INTO categories (name) VALUES
('Category 1'),
('Category 2'),
('Category 3'),
('Category 4'),
('Category 5');

INSERT INTO products (name, category_id) VALUES
('Product 1', 1),
('Product 2', 2),
('Product 3', 4),
('Product 4', 4),
('Product 5', 4);