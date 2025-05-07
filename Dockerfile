# pull python base image
FROM python:3.12

WORKDIR /app


# Copy requirements file
COPY requirements.txt .

# update pip
RUN pip install --upgrade pip

# install dependencies
RUN pip install -r requirements.txt


# copy application files & change/give ownership to myuser 
# COPY app/. app/.

# expose port for application
EXPOSE 8001

COPY . .

# start fastapi application
CMD ["python", "app.py"]