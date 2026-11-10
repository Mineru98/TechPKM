---
Language: Rust
tags:
 - macOS
 - 카카오톡
 - AI에이전트
 - 자동화
 - CLI
aliases:
 - OpenKakao
 - openkakao-cli
 - 카카오톡 자동화
url: https://github.com/JungHoonGhae/openkakao-cli
---
OpenKakao는 이미 로그인된 공식 카카오톡 Mac 앱을 macOS 손쉬운 사용(Accessibility)으로 제어하여 카카오톡 메시지 전송·읽기·백업 작업을 AI 에이전트에게 맡길 수 있게 하는 Rust 기반 CLI 도구입니다. 별도 로그인, 프로토콜 통신, DB 복호화 없이 공식 앱만 사용하며, 키보드와 마우스를 뺏지 않고 보낸 메시지는 화면에서 다시 읽어 전송을 확인합니다. Touch ID 승인, 방 등록 화이트리스트 등 안전장치를 갖추고 Claude Code 등 다양한 에이전트와 연동됩니다.