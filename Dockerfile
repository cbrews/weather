# Using community python image 3.12
FROM python:3.12

# General python environment settings
ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
WORKDIR $APP_HOME

# Load resources onto box (see .dockerignore)
COPY . .

# Dependency installation
RUN pip install --upgrade pip && pip install .

# Cleanup package artifacts
RUN rm -rf build app.egg-info

# Runtime
CMD ["python", "-m", "fastapi", "run", "app"]