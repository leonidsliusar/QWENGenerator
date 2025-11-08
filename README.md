1. Download model manually
````bash
git lfs install
mkdir -p /workspace/models
git clone https://huggingface.co/Qwen/Qwen-Image-Edit-2509 /workspace/models/Qwen-Image-Edit-2509
````

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

