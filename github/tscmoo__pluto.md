---
Language: C++
tags:
 - StarCraft-BroodWar
 - AI
 - 강화학습
 - 신경망
 - BWAPI
aliases:
 - Pluto AI
 - Pluto BWAPI bot
 - 브루드워 AI
url: https://github.com/tscmoo/pluto
---
Pluto는 StarCraft: Brood War의 1v1 대전을 위해 만들어진 AI 봇으로, 단일 신경망이 자기대행(self-play) 강화학습을 통해 매크로와 마이크로를 포함한 게임 전반을 세 종족 모두에서 스크립트 없이 수행합니다. BWAPI를 통해 동작하며, 별도의 64비트 CPU 추론 엔진과 공유 메모리로 통신하여 GPU 없이도 실시간 플레이가 가능합니다. 이 저장소는 바이너리 릴리스를 제공하며, 상대별 빌드 오더 통계 파일을 편집해 오프닝을 조정하는 등의 유저 설정 기능도 지원합니다.