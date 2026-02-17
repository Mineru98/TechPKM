---
Language: TypeScript
tags:
 - Node.js
 - Redis
 - JobQueue
 - MessageQueue
 - DistributedSystem
aliases:
 - BullMQ
 - 불큐
 - Redis Queue
url: https://github.com/taskforcesh/bullmq
---
Node.js 환경에서 Redis를 기반으로 동작하는 가장 빠르고 신뢰할 수 있는 분산형 큐 라이브러리입니다. 원자성(atomicity)과 안정성을 중시하여 설계되었으며, 작업 추가, 처리, 이벤트 리스닝 기능을 통해 백그라운드 작업을 효율적으로 관리할 수 있습니다. 특히 상위-하위 작업 간의 의존성을 설정하는 흐름(Flow) 기능과 반복 가능한 작업 스케줄링 등 고급 기능을 제공합니다.