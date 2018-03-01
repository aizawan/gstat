## Build Image
```
docker build -t gstat --build-arg admin_passwd="admin_passwd" docker/
```

## Create Container
```
docker run -d --restart=always -p 8888:8888 --name gstat -h gstat gstat
```

## How to Access
* Admin `http://your/server:8888/admin`
* Others `http://your/server:8888/cms/resource`
