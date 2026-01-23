---
Language: TypeScript  
tags:  
 - S3 클라이언트  
 - 경량 라이브러리  
 - Edge 컴퓨팅  
 - 파일 업로드  
 - 멀티파트 업로드  
aliases:  
 - s3미니  
 - s3mini  
 - S3 호환 저장소 클라이언트  
 - 경량 S3 클라이언트  
url: https://github.com/good-lly/s3mini  
---  
s3mini는 Node.js, Bun, Cloudflare Workers 등 에지 플랫폼용 초경량 S3 호환 객체 저장소 클라이언트입니다. 20KB 미만의 최소화된 크기와 초당 작업 처리량(ops/s) 15% 향상을 특징으로 하며, Cloudflare R2, Backblaze B2, MinIO 등 다양한 S3 호환 서비스에서 테스트되었습니다. 기본 S3 API(업로드, 다운로드, 삭제, 목록 조회 등)를 지원하며, 서버 측 암호화(SSE-C), 멀티파트 업로드, 조건부 요청, 에러 핸들링 기능을 제공합니다. 브라우저 환경은 지원하지 않습니다.