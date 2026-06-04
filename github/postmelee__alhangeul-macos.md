---
Language: Swift
tags:
 - macOS
 - HWP
 - QuickLook
 - SwiftUI
 - Rust
aliases:
 - 알한글
 - Alhangeul
 - alhangeul-macos
url: https://github.com/postmelee/alhangeul-macos/blob/main/README.md
---
알한글(Alhangeul)은 macOS 환경에서 HWP/HWPX 한글 문서를 미리보고, 열어보고, 저장 및 PDF로 내보낼 수 있게 해주는 오픈소스 데스크톱 유틸리티입니다. Finder의 Quick Look 및 썸네일 통합을 지원하여 별도 앱 실행 없이도 파일 내용을 바로 확인할 수 있으며, 모든 문서 처리는 업로드 없이 로컬에서 이루어집니다. Rust 기반의 rhwp 코어를 Swift/Rust 네이티브 브리지로 연동하여 닫힌 한글 문서 포맷을 Mac 네이티브 경험으로 확장하는 것을 목표로 합니다.