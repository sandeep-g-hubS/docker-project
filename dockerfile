FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /home/data

# Copy the Python script and text files to the container
COPY scripts.py /home/data
COPY IF.txt /home/data
COPY AlwaysRememberUsThisWay.txt /home/data

# Create output directory
RUN mkdir -p /home/data/output

# Run the Python script
CMD ["python", "scripts.py"]
