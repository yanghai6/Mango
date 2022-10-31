# Mango App

## Installing

### Backend

#### Installing backend server run (in root):

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

After activated virtual env, run:

```bash
(venv) $ pip3 install -r requirements.txt
```

#### Installing frontend dependencies

After activated virtual env, run in `app/static`:

```bash
(venv) $ yarn install
```

### PostgreSQL Setup

Make a .env file in `app/backend` with the following entry:

```bash
DATABASE_URL="postgresql://<user>:<password>@localhost:5432/<dbname>"
```

In the Python terminal enter the commands:

```python
from app.backend.models.shared import db
from app import create_app
app = create_app()
app.app_context().push()
db.create_all()
```

to make the tables.

## Setup envs
Need to supply these to `.env` (which is located at the base folder, eg `/mango/.env`) to run several services. Contact team [Mango-Services](https://github.com/orgs/dcsil/teams/mango-services/members) for these credentials

```bash
DATABASE_URL=""
SENTRY_URL=""
AUTH0_BASE_URL=""
AUTH0_SPA_CLIENT_ID=""
AUTH0_API_AUDIENCE=""
SECRET_KEY=""
```

## Available Scripts

In the project directory, you can run:

### Linting/Testing

```bash
black --check .
cd app/static && npx prettier --check .
pytest
```

### To start the Flask server run:

```bash
python3 run.py
```

### `yarn run build`

Creates a build for the Flask server to serve. Use for deploying.

### `yarn run watch`

Continuously updates the build as changes are made to the front end files. Use when developing.

## Troubleshoot

### If postgres not running locally:

```bash
sudo pg_ctlcluster <version> main start

#restart postgresql service
sudo service postgresql restart
```

### If app not running https locally

Add `ssl_context="adhoc"` argument to `app.run` in [run.py](./run.py) file
```python
app.run(debug=True, ssl_context="adhoc")
```
