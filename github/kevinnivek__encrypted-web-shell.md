---
Language: PHP
tags:
 - PHP
 - 암호화
 - 웹셸
 - AES-256-CBC
 - OpenSSL
aliases:
 - 암호화된 웹셸
 - PHP 코드 보호
 - 웹셸 보안
url: https://github.com/kevinnivek/encrypted-web-shell
---
이 프로젝트는 PHP 코드를 OpenSSL 라이브러리의 AES-256-CBC 암호화 방식으로 보호하는 간단한 웹셸 솔루션입니다. GET 방식 대신 POST를 통해 복호화 키를 전달하여 로깅 위험을 줄이는 것이 특징이며, eval 함수를 통해 암호화된 코드를 실행합니다. 웹셸, 침투 테스트, 원격 시스템 관리 등에서 코드 난독화 및 보안 강화에 활용될 수 있습니다.  

암호화된 코드는 웹 폼을 통해 키를 입력하면 쿠키에 저장되고 자동으로 실행되며, PHP의 OpenSSL 확장 기능을 활용한 다양한 암호화 옵션 적용이 가능합니다.