FROM python:3.8.0-buster

# Create and set working dir to /app
RUN mkdir /app
WORKDIR /app

# Install neccesary system dependencies
RUN pip install pipenv

# Copy Pipfile and Pipefile.lock
COPY Pipfile* ./

# Install neccesary app dependencies
RUN pipenv install --system --deploy --ignore-pipfile

# Copy the rest of the source code for the app
COPY . .

# Set up to run the src/main python script on container startup
CMD [ "python", "src/main.py" ]
