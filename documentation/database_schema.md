# **Database Schema**

## `users`
| Users       | data type | details                   |
|-------------|-----------|---------------------------|
| id          | integer   | not null, primary key     |
| username    | string    | not null,                 |
| email       | string    | not null, indexed, unique |
| password    | string    | not null                  |
| created_at  | datetime  | not null                  |
| updated-at  | datetime  | not null                  |

| rship name  | table     | back_populates        |
|-------------|-----------|-----------------------|
| films       | films     | user                  |
| people      | people    | user                  |
| reviews     | reviews   | user                  |
| seen        | seen_films| user                  |

## `films`
| column name | data type | details               |
|-------------|-----------|-----------------------|
| id          | integer   | not null, primary key |
| userId      | integer   | not null, foreign key |
| title       | string    | not null              |
| genre       | string    | not null              |
| year        | integer   | not null              |
| duration    | integer   | not null              |
| year        | integer   | not null              |
| synopsis    | string    | not null              |
| key_art     | string    | not null              |
| cover-photo | string    |                       |
| created_at  | datetime  | not null              |
| updated-at  | datetime  | not null              |

| rship name  | table     | back_populates        |
|-------------|-----------|-----------------------|
| user        | users     | films                 |
| reviews     | reivew    | film                  |
| seen        | seen_films| film                  |

## `people`
| column name | data type | details               |
|-------------|-----------|-----------------------|
| id          | integer   | not null, primary key |
| userId      | integer   | not null, foreign key |
| name        | string    | not null              |
| featured_photo| string  |                       |
| bio         | string    |                       |
| born        | date      |                       |
| created_at  | datetime  | not null              |
| updated-at  | datetime  | not null              |

| rship name  | table     | back_populates        |
|-------------|-----------|-----------------------|
| user        | users     | people                |

## `roles` (Join table on films/people)
| column name | data type | details               |
|-------------|-----------|-----------------------|
| id          | integer   | not null, primary key |
| filmId      | integer   | not null, foreign key |
| personId    | integer   | not null, foreign key |
| role        | string    | not null,             |
| created_at  | datetime  | not null              |
| updated-at  | datetime  | not null              |

| rship  name | table     | back_populates        |
|-------------|-----------|-----------------------|
| film        | films     | roles                 |
| person      | people    | roles                 |


## `reviews`
| column name | data type | details               |
|-------------|-----------|-----------------------|
| id          | integer   | not null, primary key |
| userId      | integer   | not null, foreign key |
| filmId      | integer   | not null, foreign key |
| rating      | integer   |                       |
| review_text | integer   | not null              |
| created_at  | datetime  | not null              |
| updated-at  | datetime  | not null              |

| rship name  | table     | back_populates        |
|-------------|-----------|-----------------------|
| user        | users     | reviews               |
| film        | films     | reviews               |

## `seen_films`
| column name | data type | details               |
|-------------|-----------|-----------------------|
| id          | integer   | not null, primary key |
| filmId      | integer   | not null, foreign key |
| userId      | integer   | not null, foreign key |

| rship name  | table     | back_populates        |
|-------------|-----------|-----------------------|
| user        | users     | seen                  |
| film        | films     | seen                  |
