---
Language: Dockerfile  
tags:  
 - Docker  
 - Hadoop  
 - Spark  
 - 빅데이터  
 - 분산처리  
aliases:  
 - HDFS-Spark 워크벤치  
 - Docker 기반 Hadoop/Spark 환경  
 - 빅데이터 개발 환경  
url: https://github.com/big-data-europe/docker-hadoop-spark-workbench  
---  
이 프로젝트는 Docker를 사용해 HDFS/Spark 워크벤치 환경을 쉽게 구축할 수 있도록 설계된 도구입니다. 로컬 환경에서 빅데이터 처리 시스템을 신속하게 테스트하거나 개발할 수 있는 목적을 가지며, Hive 및 Hue 인터페이스를 통한 데이터 관리 기능을 추가로 지원합니다. README에 명시된 대로 Docker Compose와 Swarm 설정을 통해 단일/분산 환경을 구성할 수 있으며, EU 프로젝트에서 개발되었으나 현재는 활발히 유지보수되지 않습니다.  

(참고: README에서 추론한 주요 언어는 Dockerfile이지만, 실제 구현에는 Bash, YAML, Scala/Spark 코드 예제가 포함되어 있습니다)