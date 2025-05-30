# Object Relations Code Challenge

A Python project for practicing object-relational mapping (ORM) concepts, database schema design, and Python OOP. This project simulates a publishing platform with Authors, Magazines, and Articles, providing a hands-on approach to understanding relationships between objects and persistent storage.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- Models for Authors, Magazines, and Articles
- SQLite database integration
- Example scripts for database setup and queries
- Unit tests for all models

## Project Structure

```
code-challenge/
  lib/
    controllers/
    db/
    models/
    debug.py
  scripts/
    run_queries.py
    setup_db.py
  tests/
    test_article.py
    test_author.py
    test_magazine.py
  README.md
articles.db
Pipfile
Pipfile.lock
```

- **lib/models/**: Core Python classes for Author, Magazine, and Article
- **lib/db/**: Database connection, schema, and seed data
- **lib/controllers/**: (Reserved for future business logic)
- **scripts/**: Utility scripts for setup and running queries
- **tests/**: Unit tests for all models

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd object-relations
   ```
2. **Install dependencies:**
   ```bash
   pipenv install
   pipenv shell
   ```
3. **Set up the database:**
   ```bash
   python code-challenge/scripts/setup_db.py
   ```

## Usage

- Run the database seed script to populate sample data:
  ```bash
  python code-challenge/lib/db/seed.py
  ```
- Run example queries:
  ```bash
  python code-challenge/scripts/run_queries.py
  ```
- Explore and modify models in `lib/models/` to practice OOP and ORM concepts.

## Testing

Run all tests using:

```bash
pytest code-challenge/tests/
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss your ideas.

## License

This project is licensed under the MIT License.
