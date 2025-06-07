FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install dependencies
RUN pip install fastapi uvicorn scikit-learn joblib pydantic numpy

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]