---
Language: JavaScript/TypeScript, Python  
tags:  
 - OCR  
 - 문서변환  
 - AI처리  
 - 마크다운생성  
 - 멀티모달모델  
aliases:  
 - Zerox  
 - 문서OCR  
 - PDF마크다운변환  
 - AI문서처리  
url: https://github.com/getomni-ai/zerox  
---
Zerox는 문서를 이미지 시리즈로 변환한 후 GPT 모델에 전달하여 마크다운 형식으로 변환하는 오픈소스 도구입니다. PDF, DOCX, 이미지 등 다양한 형식을 지원하며, OpenAI, Azure OpenAI, AWS Bedrock, Google Gemini 등 다양한 AI 모델과 연동됩니다. Node.js와 Python SDK를 제공하며, 레이아웃/표/차트 등 복잡한 문서 구조를 유지하면서 텍스트를 추출할 수 있습니다. 사용자가 직접 선택한 페이지만 처리하거나, 데이터 스키마를 통해 구조화된 정보를 추출하는 기능도 지원합니다.  

핵심 특징:  
1. 다중 AI 모델 지원 (OpenAI GPT-4o, Claude, Gemini 등)  
2. Node.js/Python SDK 제공  
3. 표/레이아웃 유지를 위한 `maintainFormat` 옵션  
4. 페이지 단위 추출 및 데이터 스키마 기반 구조화  
5. PDF/DOCX/이미지 등 20+ 파일 형식 지원  
6. Discord 커뮤니티 및 호스팅 데모 제공 (https://getomni.ai/ocr-demo)