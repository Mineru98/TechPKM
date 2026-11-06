---
Language: Python
tags:
 - video-analysis
 - AI-agent
 - reverse-engineering
 - CLI
 - video-remake
aliases:
 - rea-video
 - REA Video
 - 영상 리버스 엔지니어링
url: https://github.com/JuneYaooo/rea-video
---
rea-video는 어떤 영상이든(토킹헤드, AI 영상, 3D, 모션 그래픽 등) 샷 단위로 역설계하여 시각, 편집, 오디오가 어떻게 만들어졌는지 분석하고 재제작 계획을 제공하는 CLI 도구입니다. Claude Code나 Codex 같은 AI 에이전트와 함께 실행되도록 설계되었으며, 오프라인 도구만으로도 높은 정확도(99% 내외)로 실사/AI 생성/코드 기반 영상을 구분합니다. 분석 결과는 HTML 리포트로 제공되며, 촬영 계획, AI 생성 프롬프트, Remotion 코드 접근법 등을 포함합니다.