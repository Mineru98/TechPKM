---
Language: TypeScript
tags:
 - Serverless Framework
 - AWS Lambda
 - OpenAPI 문서화
 - TypeScript 지원
 - Notion 통합
aliases:
 - slsberry
 - Serverless YML 자동 생성기
 - AWS Serverless 개발 프레임워크
url: https://github.com/spark323/slsberry
---
slsberry는 AWS Lambda 기반의 Serverless 개발을 간소화하는 프레임워크로, 소스 코드 내 `apiSpec` 정의를 기반으로 Serverless Framework `yml` 파일을 자동 생성하고 OpenAPI 3.0 및 Notion 문서화를 지원합니다. 템플릿 기반 구성, 다양한 이벤트 소스(REST API, S3, SQS 등), 환경별 배포 관리 기능을 제공하며, TypeScript를 통한 타입 안전성을 확보합니다.  

주요 특징으로는 `serverless_template.yml`과의 통합을 통한 공통 리소스 관리, 스테이지/버전 기반 배포, CLI를 통한 문서 생성(OpenAPI/Notion) 등이 있습니다. Lambda 함수 경로와 API 경로를 매핑하여 자동으로 엔드포인트를 구성하며, Windows/Linux/macOS 크로스 플랫폼 호환성을 갖추고 있습니다.