---
Language: JavaScript
tags:
 - Job Queue
 - MySQL
 - Job 처리
 - 분산 작업
 - 고성능 큐
aliases:
 - 옥센 큐
 - Oxen Queue
 - MySQL 기반 작업 큐
url: https://github.com/opteo/oxen-queue
---
Oxen Queue는 MySQL을 백엔드로 사용하는 간결한 고성능 작업 큐 시스템입니다. 수백만 건의 작업을 높은 동시성으로 처리할 수 있으며, 작업 지속성, 우선순위, 중복 제거, 지연 작업 등의 기능을 제공합니다. 사용자 정의 SQL 쿼리 실행과 기존 MySQL 인프라 활용이 필요한 경우 적합하며, Kafka나 다른 메시지 브로커를 추가하지 않으려는 팀에게 이상적입니다. 처리 속도보다 처리량을 중시하는 대규모 작업 처리 시나리오에 최적화되어 있습니다.