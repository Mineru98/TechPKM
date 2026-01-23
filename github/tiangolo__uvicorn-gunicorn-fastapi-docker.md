---
Language: Python  
tags:  
 - FastAPI  
 - Docker  
 - Uvicorn  
 - Gunicorn  
aliases:  
 - uvicorn-gunicorn-fastapi  
 - fastapi-docker-image  
url: https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker  
---  
이 프로젝트는 FastAPI 웹 애플리케이션을 위한 고성능 Docker 이미지를 제공합니다. Uvicorn과 Gunicorn을 결합하여 CPU 코어 수에 따라 자동으로 조정되는 워커를 관리하며, 단순한 배포 환경에서 높은 성능을 달성할 수 있도록 설계되었습니다. 그러나 현재는 Uvicorn의 `--workers` 옵션으로 대체될 수 있어 더 이상 권장되지 않습니다. README에는 Kubernetes와 같은 클러스터 환경에서는 별도의 컨테이너 복제 방식을 사용하는 것이 더 효과적이라는 경고가 포함되어 있습니다.  

이미지 태그는 Python 3.10 및 3.11 버전을 지원하며, Alpine 버전은 Python 프로젝트에 적합하지 않을 수 있음을 명시하고 있습니다. 주요 기능으로 환경 변수를 통한 커스터마이징, 사전 시작 스크립트 지원, Gunicorn 설정 파일 사용 등을 제공합니다.