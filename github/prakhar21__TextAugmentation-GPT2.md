# GPT-2 한국어 텍스트 생성 프로젝트

## 개요
이 프로젝트는 Hugging Face의 Transformers 라이브러리를 활용하여 GPT-2 모델을 한국어 텍스트 생성에 맞게 파인튜닝하는 것을 목표로 합니다. 기존 영어 기반 GPT-2 모델을 한국어 데이터에 적응시켜 자연스러운 한국어 문장을 생성할 수 있도록 구현했습니다.

## 주요 기능

1. **모델 다운로드**: Hugging Face에서 사전 학습된 `gpt2-medium` 모델을 자동으로 다운로드
2. **데이터 전처리**: 한국어 텍스트 데이터를 토큰화하고 모델 입력 형식에 맞게 처리
3. **파인튜닝**: 한국어 데이터로 모델을 추가 학습하여 언어 특성 반영
4. **텍스트 생성**: 파인튜닝된 모델로 자연스러운 한국어 텍스트 생성 기능 구현
   - Top-k 및 Top-p 샘플링 기법 적용
   - 온도와 반복 페널티 파라미터로 생성 다양성 제어

## 실행 방법

1. 프로젝트 클론
```bash
git clone https://github.com/yourusername/gpt2-korean.git
cd gpt2-korean
```

2. 필요한 라이브러리 설치
```bash
pip install -r requirements.txt
```

3. 파인튜닝 실행
```bash
python train.py \
  --dataset_path="data/korean_texts.txt" \
  --model_type="gpt2-medium" \
  --output_dir="fine_tuned_models/" \
  --overwrite_output_dir \
  --per_device_train_batch_size=4 \
  --gradient_accumulation_steps=4 \
  --num_train_epochs=3 \
  --save_steps=500 \
  --save_total_limit=2 \
  --logging_steps=100 \
  --learning_rate=5e-5 \
  --warmup_steps=500 \
  --weight_decay=0.01 \
  --adam_epsilon=1e-8 \
  --max_grad_norm=1.0 \
  --logging_dir="./logs" \
  --do_train
```

4. 텍스트 생성 실행
```bash
python generate.py \
  --model_name_or_path="fine_tuned_models/checkpoint-500" \
  --length=100 \
  --top_k=50 \
  --top_p=0.95 \
  --temperature=0.7 \
  --repetition_penalty=1.2 \
  --num_return_sequences=5 \
  --prompt="한국어 텍스트 생성은"
```

## 주요 파라미터 설명

| 파라미터 | 설명 |
|---------|------|
| `top_k` | 다음 단어로 선택할 상위 k개의 토큰 후보 |
| `top_p` | 누적 확률이 이 값을 넘는 토큰 집합에서 선택 (Nucleus sampling) |
| `temperature` | 생성 결과의 무작위성 조절 (0.1~1.0) |
| `repetition_penalty` | 동일 단어 반복 억제 강도 |

## 성능 최적화
- Intel DevCloud GPU 환경에서 테스트 및 검증 완료
- 첫 실행 시 모델 다운로드 및 파인튜닝으로 인한 초기 지연 발생
- 배치 처리와 그래디언트 누적 기법으로 메모리 효율성 향상

## 활용 사례
- 챗봇 대화 생성
- 문장 완성 시스템
- 언어 생성 모델 연구
- 콘텐츠 자동 생성

## 참고 문헌
- [Hugging Face Transformers Documentation](https://huggingface.co/transformers/)
- [Top-k and Top-p Sampling 논문](https://arxiv.org/pdf/1904.09751.pdf)

## 라이선스
MIT License - 상업적/비상업적 사용 모두 가능 (단, 원본 출처 명시 필요)

> 주의: 파인튜닝 품질은 학습 데이터의 양과 질에 크게 의존합니다. 최적의 결과를 얻으려면 도메인 특화된 고품질 한국어 데이터셋 사용이 권장됩니다.