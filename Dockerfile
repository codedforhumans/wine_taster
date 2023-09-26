# Use the official Python image
FROM python:3.9
#
# Set the working directory inside the container
WORKDIR /

# Copy the local app directory to the container
COPY . /

# Install app dependencies
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8050

# Run the app
CMD ["python", "app.py"]