# FastAPI Project Structure

## Root Directory

```
📦FastAPI
 ┣ 📂app
 ┃ ┣ 📂api
 ┃ ┣ 📂db
 ┃ ┃ ┗ 📜prisma_client.py
 ┃ ┣ 📂job
 ┃ ┃ ┗ 📜cron_job.py
 ┃ ┣ 📂models
 ┃ ┃ ┗ 📜model.pt
 ┃ ┣ 📂response
 ┃ ┣ 📂schema
 ┃ ┣ 📂service
 ┃ ┣ 📂utils
 ┃ ┗ 📜server.py
 ┣ 📂docs
 ┣ 📂logs
 ┣ 📂prisma
 ┃ ┣ 📜partial_types.py
 ┃ ┗ 📜schema.prisma
 ┣ 📂tests
 ┣ 📜.env
 ┣ 📜.env.example
 ┣ 📜.gitattributes
 ┣ 📜.gitignore
 ┣ 📜config.py
 ┣ 📜main.py
 ┣ 📜poetry.lock
 ┣ 📜pyproject.toml
 ┗ 📜README.md
```

## Explanation

- **Root Directory**: Contains project-wide configuration files and entry points.

  - **app**: Main application directory containing various modules and services.

    - **api**: Contains route handlers.
      - Defines API endpoints and their functions.
    
    - **db**: Database-related files.
      - `prisma_client.py`: Setup for Prisma client to interact with the database.
    
    - **job**: Scheduled jobs and background tasks.
      - Includes jobs like cron jobs or S3 bucket tasks.
    
    - **models**: Machine Learning models.
    
    - **response**: Custom response handlers and structures.
    
    - **schema**: Pydantic schemas for data validation and serialization.
    
    - **service**: Business logic and service functions.
      - Contains complex functions used in API calls.
    
    - **utils**: Utility functions and helper modules.
    
    - `server.py`: Initializes and configures the FastAPI server.

  - **docs**: Project documentation files.

  - **logs**: Daily logs files.

  - **prisma**: Prisma ORM related files.
    - `partial_types.py`, `schema.prisma`: Prisma schema and type definitions.

  - **tests**: Unit and integration test files.

  - `.env`: Environment configuration file.
  - `.env.example`: Example environment configuration file that is not ignored by Git.
  - `.gitattributes`, `.gitignore`: Git configuration files to manage attributes and ignored files.
  - `config.py`: General project configurations, such as loading environment keys.
  - `main.py`: Entry point for the application.
  - `poetry.lock`, `pyproject.toml`: Dependency management files used by Poetry.
  - `README.md`: Documentation providing an overview and instructions for the project.