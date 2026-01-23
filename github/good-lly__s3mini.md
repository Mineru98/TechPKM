---
Language: TypeScript  
tags:  
 - S3 클라이언트  
 - 경량화  
 - 에지 컴퓨팅  
aliases:  
 - s3mini  
 - 경량 S3 클라이언트  
 - S3 호환 스토리지  
url: https://github.com/good-lly/s3mini/blob/dev/README.md  
---  
s3mini는 S3 호환 객체 스토리지를 위한 초경량 TypeScript 클라이언트 라이브러리입니다. 약 20KB의 작은 크기와 빠른 성능(기존 대비 약 15% 더 높은 작업 처리 속도)을 자랑하며, Node.js, Bun, Cloudflare Workers 등의 환경에서 작동하도록 설계되었습니다. Cloudflare R2, Backblaze B2, DigitalOcean Spaces 등 다양한 S3 호환 서비스와 호환되며, 기본적인 S3 API(업로드, 다운로드, 목록 조회, 삭제 등)와 멀티파트 업로드를 지원합니다. 브라우저 환경은 지원하지 않습니다.  

주요 특징으로는 의존성 없음, AWS SigV4 서명 및 SSE-C 헤더 지원, 트리 쉐이킹 가능한 ES 모듈, TypeScript 지원 등이 있으며, Edge Computing 및 경량화된 서버리스 아키텍처에 최적화되어 있습니다.