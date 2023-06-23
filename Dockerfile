# Deriving the python image
FROM python:3.8

# Copies the requirements into the image
COPY requirements.txt /requirements.txt

# Installs all the libraries we will need to execute the code
RUN pip install -r requirements.txt

# Create a working directory in Docker, makes life easier when running instructions
WORKDIR /app

# Copies all the source code into our directory to the Docker image
COPY . /app

# Tell Docker the command to run inside the container
CMD ["python", "./main.py"]