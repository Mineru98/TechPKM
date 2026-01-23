---
Language: Python  
tags:  
 - GUI 벤치마크  
 - MLLM 평가  
 - 멀티모달 에이전트  
 - 오픈소스 프로젝트  
 - smolagents  
aliases:  
 - ScreenSuite  
 - GUI 에이전트 벤치마크  
 - ScreenBench  
 - MLLM GUI 평가  
url: https://github.com/huggingface/screensuite  
---  
ScreenSuite는 GUI 에이전트(스크린 기반 작업을 수행하는 에이전트)의 핵심 능력인 **인지, 단일 단계 및 다중 단계 행동**을 평가하기 위한 종합 벤치마크 스위트입니다. 이 프로젝트는 에이전트 구현체가 아닌 **MLLM(Multimodal Large Language Model)**의 성능을 비교하는 데 초점을 맞추며, 간단한 에이전트 구현을 위해 [smolagents](https://github.com/huggingface/smolagents)를 활용합니다. 웹, 모바일, 데스크톱 플랫폼에서의 벤치마크를 지원하며, 다양한 데이터셋과 평가 환경을 통합해 제공합니다. 주요 기술 스택은 Python이며, Docker 및 KVM 가상화 지원이 필요한 멀티스텝 벤치마크도 포함됩니다.