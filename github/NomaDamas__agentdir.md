---
Language: Rust
tags:
 - VirtualFileSystem
 - CoW
 - AI-Agent
 - CrossPlatform
 - FileManagement
aliases:
 - agentdir
 - 에이전트 디렉토리
 - 가상 파일 트리
url: https://github.com/NomaDamas/agentdir/blob/main/README.md
---
AI 에이전트와 스크립트를 위해 최적화된 읽기 전용 가상 파일 트리를 제공하는 Rust 기반 인프라 프로젝트입니다. 원본 파일을 이동시키지 않고 작업 목적에 맞는 폴더 구조를 생성하며, CoW 지원 파일 시스템에서는 데이터 중복 없이 리플링크를 활용합니다. macOS, Linux, Windows를 지원하며 Rust 라이브러리, CLI, Python, Node.js 바인딩으로 제공됩니다.