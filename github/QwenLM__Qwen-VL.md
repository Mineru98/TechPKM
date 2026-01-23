---
Language: Python  
tags:  
 - 멀티모달 AI  
 - 비전-언어 모델  
 - OCR  
 - 이미지 캡셔닝  
 - 딥러닝  
aliases:  
 - Qwen-VL  
 - Qwen-VL-Chat  
 - Qwen-VL-Plus  
 - Qwen-VL-Max  
url: https://github.com/QwenLM/Qwen-VL  
---
Qwen-VL은 알리바바 클라우드에서 개발한 멀티모달 대규모 언어 모델(Qwen 시리즈)의 비전 확장 버전입니다. 이미지, 텍스트, 바운딩 박스를 입력으로 받아들이고 텍스트 및 바운딩 박스를 출력하며, 영문 및 중문 대화가 가능하고 고해상 이미지(최대 100만 픽셀)와 극단적 종횡비 이미지를 지원합니다. 기존 오픈소스 LVLM 모델 대비 우수한 성능을 보이며, DocVQA, ChartQA, TextVQA 등 다양한 벤치마크에서 SOTA를 달성했습니다. 특히 중문 텍스트 인식 및 이해에서 GPT-4V, Gemini Ultra와 경쟁 가능한 성능을 보입니다.  

Qwen-VL-Chat, Qwen-VL-Plus, Qwen-VL-Max 등 세 가지 버전이 제공되며, 모델 스코프, 허깅페이스, 웹 페이지, API 등을 통해 무료로 접근 가능합니다. 주요 기술 혁신으로는 이미지 해상도 확장(448x448), 세부 텍스트 인식/분석 강화, 추론 능력 향상 등이 포함됩니다.  

---

### 요약  
Qwen-VL은 이미지와 텍스트를 이해하는 알리바바 클라우드의 멀티모달 대규모 언어 모델입니다. 고해상 이미지 처리, 텍스트 인식, 중문/영문 대화, 바운딩 박스 생성 기능을 갖추며, DocVQA, ChartQA 등 다양한 벤치마크에서 최고 성능을 기록했습니다. Qwen-VL-Chat, Qwen-VL-Plus, Qwen-VL-Max 등 세 가지 버전이 제공되며, 모델 스코프/허깅페이스/웹/앱/API를 통해 무료로 사용 가능합니다. 특히 중문 텍스트 이해에서 GPT-4V, Gemini Ultra 수준의 성능을 보입니다.  

---

### 기술 스택  
- **기반 모델**: Qwen-7B + OpenClip ViT-bigG  
- **지원 기능**:  
  - 다중 이미지 입력 및 비교  
  - 이미지 기반 다중 질문/답변  
  - 창의적 기능 (예: 시 생성)  
  - 중문/영문 텍스트 인식 및 이해  
  - 바운딩 박스 생성 (객체 위치 지정)  
- **주요 향상 요소**:  
  - 448x448 해상도 지원으로 세부 텍스트 인식 향상  
  - 극도로 긴 종횡비 이미지 처리  
  - 복잡한 수학적/시각적 추론 능력  

---

### 평가 결과  
- **DocVQA**: 93.1% (Gemini Ultra 90.9%, GPT-4V 88.4%)  
- **ChartQA**: 79.8% (Gemini Ultra 80.8%)  
- **TextVQA**: 79.5% (GPT-4V 78.0%)  
- **MMMU**: 51.4% (Gemini Ultra 59.4%)  
- **MathVista**: 51.0% (Gemini Ultra 53.0%)  
- **MM-Bench-CN**: 75.1% (Gemini Pro 74.3%)  

---

### 사용법  
1. **환경 설정**:  
   ```bash
   pip install -r requirements.txt
   pip install optimum  # 양자화 모델 사용 시  
   pip install deepspeed  # 파인튜닝 시  
   pip install peft  # LoRA/Q-LoRA 사용 시  
   ```

2. **기본 사용법 (트랜스포머)**:  
   ```python
   from transformers import AutoModelForCausalLM, AutoTokenizer

   tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-VL-Chat", trust_remote_code=True)
   model = AutoModelForCausalLM.from_pretrained(
       "Qwen/Qwen-VL-Chat", device_map="auto", trust_remote_code=True, fp16=True
   ).eval()

   # 이미지 분석 예시
   response, history = model.chat(
       tokenizer,
       query=">https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg</img> 이 사진은 무엇인가요?",
       history=None
   )
   print(response)  # "이미지에는 한 여성이 해변에서 개와 놀고 있습니다. 개는 래브라도 종입니다."
   ```

3. **양자화 모델 (Int4) 사용**:  
   ```python
   model = AutoModelForCausalLM.from_pretrained(
       "Qwen/Qwen-VL-Chat-Int4", device_map="auto", trust_remote_code=True
   ).eval()
   ```

4. **웹 데모 실행**:  
   ```bash
   python web_demo_mm.py
   ```

---

### 파인튜닝  
- **지원 방식**:  
  - 전체 파라미터 파인튜닝  
  - LoRA (저비용 파인튜닝)  
  - Q-LoRA (양자화 모델 기반 파인튜닝)  
- **데이터 준비**:  
  - JSON 형식의 대화 데이터 필요 (이미지 경로: `<img>이미지 경로</img>`)  
  - 바운딩 박스 표현: `<ref>객체 설명</ref><box>(x1,y1),(x2,y2)</box>`  
- **실행 예시 (LoRA)**:  
  ```bash
  sh finetune/finetune_lora_ds.sh
  ```

---

### 성능 비교  
| 방법 | 384 토큰 | 512 토큰 | 1024 토큰 | 2048 토큰 |  
|------|----------|----------|-----------|-----------|  
| LoRA (기본) | 37.1G / 2.3s/it | 37.3G / 2.4s/it | 38.7G / 3.6s/it | 38.7G / 6.1s/it |  
| LoRA (챗) | 23.3G / 2.2s/it | 23.6G / 2.3s/it | 25.1G / 3.5s/it | 27.3G / 5.9s/it |  
| Q-LoRA | 17.0G / 4.2s/it | 17.2G / 4.5s/it | 18.2G / 5.5s/it | 19.3G / 7.9s/it |  

---

### 라이선스  
- 연구 및 상업적 사용 가능. 자세한 내용은 [LICENSE](LICENSE) 참조.  
- 모델 사용 시 [논문](https://arxiv.org/abs/2308.12966) 인용 권장.  

```BibTeX
@article{Qwen-VL,
  title={Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond},
  author={Bai, Jinze and Bai, Shuai and Yang, Shusheng and Wang, Shijie and Tan, Sinan and Wang, Peng and Lin, Junyang and Zhou, Chang and Zhou, Jingren},
  journal={arXiv preprint arXiv:2308.12966},
  year={2023}
}
```