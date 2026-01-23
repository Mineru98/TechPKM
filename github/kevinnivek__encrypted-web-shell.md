---
Language: PHP  
tags:  
 - 암호화  
 - 웹 쉘  
 - AES-256-CBC  
 - 보안 도구  
 - 코드 난독화  
aliases:  
 - 암호화 웹 쉘  
 - PHP 보안 도구  
 - AES-256-CBC 암호화  
 - 코드 난독화 도구  
url: https://github.com/example/encrypted-web-shell  
---  
이 프로젝트는 OpenSSL 라이브러리의 AES-256-CBC 암호화 방식을 활용하여 PHP 코드를 보호하는 간단한 웹 쉘 솔루션입니다. GET 요청 대신 POST 방식으로 복호화 키를 전달받아 로깅 위험을 줄이는 것이 핵심 특징이며, 코드 난독화를 통해 쉘 또는 원격 관리 도구의 보안성을 향상시킬 수 있습니다. 암호화된 코드는 쿠키 기반 키 인증 후 eval로 실행되며, 기본적인 설치 및 사용법 가이드라인이 제공됩니다.