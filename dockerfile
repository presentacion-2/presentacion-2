# Base image with Python and Node.js
#FROM --platform=linux/amd64 node:latest

FROM node:latest

# Install Google Chrome Stable and fonts
# Note: this installs the necessary libs to make the browser work with Puppeteer.
#RUN apt-get update && apt-get install gnupg wget -y && \
#    wget --quiet --output-document=- https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /etc/apt/trusted.gpg.d/google-archive.gpg && \
#    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
#    apt-get update && \
#    apt-get install google-chrome-stable -y --no-install-recommends && \
#    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the source code to the working directory
COPY . /app

# Install Python and create a virtual environment
RUN apt-get update && apt-get install -y python3 python3-venv
RUN python3 -m venv /venv

# Activate the virtual environment and install Python dependencies
ENV PATH="/venv/bin:$PATH"
RUN pip install -r biblioteca-app/api/requirements.txt

# Install Node.js dependencies
RUN cd biblioteca-app/frontend && \
    npm install --force


EXPOSE 22

# Define the command to run the applications
CMD ["sh", "-c", "python3 biblioteca-app/api/main.py & npm start --prefix biblioteca-app/frontend"]

