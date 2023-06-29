FROM selenium/node-firefox

WORKDIR /app

COPY . /app

USER root

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs

RUN sudo apt-get update && apt-get install -y python3 python3-venv python3-pip
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip3 install -r biblioteca-app/api/requirements.txt

# Install Node.js dependencies
RUN cd biblioteca-app/frontend && \
    npm install --force

EXPOSE 5000

# Define the command to run the applications
RUN chown -R seluser:seluser /app
USER seluser
CMD ["sh", "-c", "python3 biblioteca-app/api/main.py & npm start --prefix biblioteca-app/frontend"]
