create table if not exists Audiobooks (
    id int not null autoincrement,
    name varchar(255) not null,
    author varchar(255) not null,
    description varchar(500),
    storage_url varchar(255),
    date_created date,
    audio_position_seconds int
)
