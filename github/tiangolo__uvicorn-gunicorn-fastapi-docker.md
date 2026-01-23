---
Language: Python
tags:
 - FastAPI
 - Docker
 - Uvicorn
 - Gunicorn
 - ASGI
aliases:
 - uvicorn-gunicorn-fastapi
 - FastAPI Docker 이미지
 - Uvicorn+Gunicorn 컨테이너
 - Python 웹 서버
url: https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
---
이 프로젝트는 더 이상 사용되지 않는 Docker 이미지로, FastAPI 웹 애플리케이션을 위한 고성능 Uvicorn과 Gunicorn 조합을 제공합니다. CPU 코어 수에 따라 자동 조정되는 워커 프로세스를 통해 단일 컨테이너에서 높은 성능을 달성할 수 있도록 설계되었습니다. Kubernetes 등의 클러스터 관리 시스템을 사용하는 경우 이 이미지 대신 직접 Docker 이미지를 빌드하고 Uvicorn의 `--workers` 옵션을 사용하는 것이 권장됩니다. Python 3.10 및 3.11 버전을 지원하며, Docker Hub에서 다양한 태그로 제공됩니다. FastAPI, Uvicorn, Gunicorn, ASGI 프레임워크와 관련된 기술 스택을 사용하는 프로젝트에 적합합니다.