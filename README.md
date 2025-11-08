1. Download model manually
````bash
git lfs install
mkdir -p /workspace/models
git clone https://huggingface.co/Qwen/Qwen-Image-Edit-2509 /workspace/models/Qwen-Image-Edit-2509
````

2. Secure copy manually
```bash
scp -P 13742 -r ./app root@91.150.160.38:/workspace/
scp -P 13742 ./requirements.txt root@91.150.160.38:/workspace/
```

3. Run script manually
```bash
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.11 python3.11-venv python3.11-dev
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3.11 -m app.main
```

2. Install nginx
```bash
sudo apt update
sudo apt install nginx
```

3. Config nginx
```bash
sudo nano /etc/nginx/sites-available/myapp
```
```nano
server {
    listen 80 default_server;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

```bash (check config)
sudo nginx -t
```

```bash (start)
sudo nginx
```

2. Docker start
```bash
docker run -v /workspace/Qwen-Image-Edit-2509:/app/model your_docker_image
```

3. Compose start
```bash

```

4. Run locally
```bash
python -m app.main
```

