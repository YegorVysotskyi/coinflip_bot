## Coinflip Telegram Bot

## System Requirements
- Python 3.10^
- Docker

### Local Startup
1. Create virtual environment with `python -m venv venv`
2. Activate the environment `source ./venv/bin/activate`
3. Install requirements with `pip install -r requirements.txt`
4. Start bot with `python -m app`

### Docker Startup
1. Build image with `docker build -t coinflip .`
2. Run container with `docker run -d --name coinflip coinflip`

### Stop Bot and Cleanup Docker
3. Stop container with docker stop coinflip
4. Remove container with docker rm coinflip
5. Remove image with docker rmi coinflip
