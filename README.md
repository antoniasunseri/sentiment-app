# Sentiment Streamlit App
The following project takes a streamlit sentiment analysis application and packages it into a standard, reproducible container using Docker. The streamlit sentiment app predicts whether a movie review is **positive** or **negative**  using a Naive Bayes model trained on the IMDB dataset.

### Prerequisites:
- Docker Installation \
**See** Docker Desktop @ https://www.docker.com/products/docker-desktop/

### How to Run:
Go to command prompt, Win +R  
- Clone the repositorary
  - git clone https://github.com/antoniasunseri/sentiment-app.git
  - cd sentiment-app

- Build the Docker image: \
Using Makefile to build image
  - Make Build
    - Command to build Docker image
  - Make Run
    - Command run to a container from Docker image and maps the container's port to a port on your local machine
    - Access the app in your browser http://localhost:8501
  - Make Clean
    - Command to delete Docker image to save space

### Tips & Troubleshooting
Go to command prompt: 
1. Verify Docker installation with 'docker --version'
2. Check running containers with command 'docker ps'
   

  
