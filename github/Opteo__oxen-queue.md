---
Language: JavaScript
tags:
 - JobQueue
 - MySQL
 - Node.js
 - Worker
 - Concurrency
aliases:
 - Oxen Queue
 - 옥센 큐
 - oxen-queue
url: https://github.com/Opteo/oxen-queue/blob/master/README.md
---
MySQL을 기반으로 동작하는 견고하고 실용적인 워커 큐 라이브러리입니다. 하루에 수백만 개의 job 처리를 목표로 높은 동시성과 처리량을 제공하며, 연결 끊김이나 비정상 job 등의 문제 상황에 유연하게 대처합니다. 별도의 큐 전용 데이터베이스 추가 없이 기존 MySQL 환경에서 SQL을 통해 직접 job 상태를 조회하고 분석할 수 있는 것이 핵심 특징입니다.