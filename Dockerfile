# Dockerfile

# 1. Base Image: Start from an official lightweight Python image
# We choose a version that matches your environment, e.g., Python 3.11 slim
FROM python:3.11-slim

# 2. Set Working Directory: Define the directory inside the container
WORKDIR /app

# 3. Copy Code: Copy your entire project directory into the container's /app folder
# The .github folder for CI/CD can be ignored if desired, but including code files is necessary.
COPY mybank.py /app/
COPY test_mybank.py /app/
COPY .github /app/
COPY .gitignore /app/

# Normal Scnario
# # 4. Command to Run: Define the default command to execute when the container starts
# # We can set it to run your unit tests as a default action to verify the container works.
# CMD ["python", "-m", "unittest", "test_mybank.py"]

# For kubernetes deployment
# 4. Command to Run: Run tests on startup, then execute an infinite loop
# This is a common pattern to keep utility/testing containers alive
CMD ["/bin/sh", "-c", "python -m unittest test_mybank.py && sleep infinity"]
