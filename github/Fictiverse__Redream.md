---
Language: C#
tags:
 - StableDiffusion
 - ControlNet
 - Screencapture
 - API_통합
 - 실시간_영상처리
aliases:
 - Redream
 - 스크린_디퓨전
 - 실시간_스테이블디퓨전
 - 화면_캡처_생성
url: https://github.com/Fictiverse/Redream
---
Fictiverse의 Redream 프로젝트는 화면 특정 영역을 실시간으로 캡처하여 Stable Diffusion 모델을 통해 이미지 생성하는 도구입니다. Automatic1111 웹UI의 API와 ControlNet 확장을 활용하여 마우스 조작을 통한 마스크 영역 지정 및 생성 파라미터 조정이 가능합니다. 주로 Windows 환경에서 .NET 6.0 기반으로 실행되며, 디퓨전 설정 프리셋 저장 및 프롬프트 보간 기능을 제공합니다.  

> 핵심 기능:  
> - 실시간 화면 캡처 영역 지정 및 마스크 편집  
> - Stable Diffusion 파라미터(스텝, 씨드, CFG 스케일 등) 마우스 조작  
> - 자동 생성된 프레임 저장 및 프리셋 관리  
> - 인터페이스 숨김 기능 지원