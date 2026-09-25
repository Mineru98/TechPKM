---
Language: Python
tags:
 - video-processing
 - scene-detection
 - ffmpeg
 - opencv
 - cli-tool
aliases:
 - PySceneDetect
 - scenedetect
 - 비디오 장면 감지
url: https://github.com/Breakthrough/PySceneDetect
---
PySceneDetect는 비디오 파일에서 장면 전환(cut)을 자동으로 감지하고 분석하는 오픈소스 파이썬 도구입니다. CLI와 Python API를 모두 제공하며, ffmpeg/mkvmerge를 활용한 장면 분할, 프레임 저장, 다양한 감지 알고리즘(ContentDetector, AdaptiveDetector, ThresholdDetector 등)을 지원합니다. Docker 이미지도 제공되어 파이프라인에 쉽게 통합할 수 있습니다.