
FROM python:3.9.7
# Set the working directory to /app
WORKDIR /flask_mvc
# Copy local contents into the container
ADD . /flask_mvc
# Install all required dependencies
RUN pip install -r requirements.txt
EXPOSE 5000
# CMD ["python", "app.py"]
CMD ["flask", "run"]