FROM ubuntu:latest

# Set the working directory.
WORKDIR ~/gap-python

# Copy the file from your host to your current location.
COPY . .

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 8080

# Run the specified command within the container.
CMD "python ~/gap-python/gap-python.py"

