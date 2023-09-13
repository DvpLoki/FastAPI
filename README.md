# My FastAPI practice 

## Introduction
This is a simple project versioned in my way to learn FastAPI.



## Setup
To set up a development environment and run the code, follow these steps:

### 1. Clone the Repository
git clone [URL]

### 2. Create a Virtual Environment (Optional but Recommended)
# On Windows
python -m venv venv

### 3. Activate the Virtual Environment
# On Windows
venv\Scripts\activate

### 4. Install Dependencies
pip install -r requirements.txt

### 5. Run the Code
 Replace App_v1.py with the name of the Python file containing  FastAPI code with appropriate version.
## uvicorn App_v1.main:app --reload




## Version 1: Basic CRUD Operations
- **Overview**: Version 1 focuses on implementing basic CRUD operations for posts.
- **Endpoints**: The following CRUD endpoints are available:
  - `POST /posts`: Create a new post.
  - `GET /posts`: Retrieve all posts.
  - `GET /posts/{id}`: Retrieve a post by ID.
   - `GET /posts/latest`: Retrieve latest created posts.
  - `PUT /posts/{id}`: Update a post by ID.
  - `DELETE /posts/{id}`: Delete a post by ID.
- **Database Changes**: None in this version (In-memory data store used).


## Version 2: PostgreSQL Integration
- **Overview**: Version 2 integrates the project with a PostgreSQL database for persistent data storage.
- **Endpoints**: The same CRUD endpoints as in Version 1 are available.
- **Database Changes**: PostgreSQL database used for data storage.


## Version 3: SQLAlchemy ORM and Alembic Data Migrations (Planned)
- **Overview**: Version 3 plans to enhance the project with SQLAlchemy ORM and Alembic for data migrations.
- **Endpoints**: (To be updated when implemented)
- **Database Changes**: (To be updated when implemented)
- **User Authentication**: (To be updated when implemented)
