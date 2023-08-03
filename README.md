# Weather App Code Challenge Overview

## Programming Language:

- Python

## Libraries and Frameworks Employed:

- Django
- Django Rest Framework (DRF)

## Data Inputs:

- Weather information, referred to as `wx_data`
- Yield information, referred to as `yld_data`

## Database Technology:

- SQLite

## Data Folder Note:

- Include the folders `wx_data` and `yld_data` in the code directory `(./)`.

## Code Structure:

- `wx_data`: Contains weather-related data input.
- `yld_data`: Contains yield-related data input.
- `src`: Houses the Django application codebase and other custom applications.
- `answers`: Holds log information generated during application usage, stored in `logfile.log`.

## Execution Instructions:

### Setting Up the Virtual Environment:

```bash
  pip install virtualenv
  virtualenv env
```

### Activating the Virtual Environment:

```bash
  env/Scripts/activate (Windows)
  source env/bin/activate (Linux and Mac)
```

### Installing Necessary Dependencies:

```bash
  pip install -r requirements.txt
```

### Migrating the Database Models:

```bash
  python src/manage.py makemigrations weather_app
  python src/manage.py migrate weather_app
```

### Insert data into SQLite DB:

```bash
  python src/manage.py ingest
```

### Starting the Development Server:

```bash
  python src/manage.py runserver
```

### Accessing the Application:

- API Documentation: http://127.0.0.1:8000/api/swagger/
- Weather Statistics: http://127.0.0.1:8000/api/weather/stats/
- Weather Data: http://127.0.0.1:8000/api/weather/
- Query Example: http://127.0.0.1:8000/api/weather/?date=20100101

## Running Tests:

```bash
  python src/manage.py test
```

# Deployment to AWS:

## Deploying Django Application:

- Utilize AWS Elastic Beanstalk to simplify the deployment, supporting Python, Django's underlying language.
- Set up a load balancer to efficiently distribute incoming traffic across multiple application instances.

## Database Deployment:

- Utilize Amazon Relational Database Service (RDS) for hosting a scalable and secure PostgreSQL database.
- Ensure proper configuration for secure communication between Django and the RDS instance.

## Data Storage Solution:

- Employ AWS EFS or S3 buckets for storing text files.

## Scheduling Data Ingestion:

- Consider using AWS ECS FARGATE for scheduling data ingestion, with ECR to house the image.
- Employ Amazon CloudWatch Events to define rules for triggering Fargate tasks at designated intervals, storing the ingested data in the RDS database.

## Conclusion:

- This approach offers a scalable, secure, and manageable deployment of your Django API, database, and data ingestion routine.
- The synergy of AWS Elastic Beanstalk, Amazon RDS, ECS FARGATE, and Amazon CloudWatch Events lets you adapt to varying traffic and run data ingestion as required, without manual infrastructure handling.

## Screenshots:

![Weather](weather.png?raw=true "weather")

![Statistics](statistics.png?raw=true "statistics")

![Swagger API](swagger_api.png?raw=true "swagger_api")

![Swagger API](response1.png?raw=true "response")

![Swagger API](response2.png?raw=true "response")
