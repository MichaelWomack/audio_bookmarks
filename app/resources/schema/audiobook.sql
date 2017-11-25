create table if not exists Audiobooks (
    id SERIAL PRIMARY KEY,
    name varchar(255) NOT NULL,
    author varchar(255),
    description varchar(500),
    publish_year INTEGER,
    storage_url varchar(255),
    created_timestamp TIMESTAMP NOT NULL,
    audio_position_seconds INTEGER
);
