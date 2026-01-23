# GPT-2를 활용한 한국어 대화 모델 미세 조정 (Fine-tuning) 프로젝트

## 📌 프로젝트 개요
이 프로젝트는 **Hugging Face Transformers**와 **한국어로 사전 훈련된 GPT-2 모델**을 활용하여, 주어진 대화 데이터셋으로 모델을 미세 조정(Fine-tuning)하는 방법을 제시합니다. 특히 "Korean-GPT2"라는 한국어 사전 훈련 모델의 가중치를 기반으로 대화 생성 성능을 향상시키기 위한 실험 환경을 구성했습니다.

## 📦 주요 의존성
- Python ≥ 3.7
- Transformers (4.21.0)
- Datasets (1.18.0)
- TensorFlow (2.9.0) 또는 PyTorch (1.10.0)
- Tokenizers (0.12.0)
- CUDA (선택적, GPU 가속 지원)

## 📂 데이터셋 구조
```
data/
├── train.txt      # 훈련용 대화 데이터 (형식: [UTTERANCE]대화 내용)
└── validation.txt # 검증용 대화 데이터
```

## ⚙️ 실행 명령어
```bash
# 1. 모델 다운로드 (최초 1회)
python download_model.py

# 2. 데이터 전처리
python preprocess_data.py \
  --input_dir data/ \
  --tokenized_dir tokenized/ \
  --model_type gpt2 \
  --max_length 128

# 3. 모델 미세 조정 (GPU 권장)
python train.py \
  --model_name_or_path "./Korean-GPT2" \
  --train_file "tokenized/train.txt" \
  --validation_file "tokenized/validation.txt" \
  --output_dir "./gpt2_finetuned" \
  --overwrite_output_dir \
  --per_device_train_batch_size 4 \
  --per_device_eval_batch_size 4 \
  --num_train_epochs 3 \
  --save_steps 10000 \
  --save_total_limit 2 \
  --prediction_loss_only \
  --learning_rate 5e-5 \
  --weight_decay 0.01 \
  --adam_epsilon 1e-8 \
  --max_grad_norm 1.0 \
  --warmup_steps 500 \
  --fp16

# 4. 대화 생성 테스트
python generate.py \
  --model_name_or_path "./gpt2_finetuned" \
  --prompt "안녕하세요" \
  --length 200 \
  --top_k 50 \
  --top_p 0.95 \
  --temperature 0.7
```

## 📊 핵심 파라미터 설명
| 파라미터 | 설명 | 권장값 |
|---------|------|--------|
| `top_k` | 상위 k개 토큰만 고려 | 40~50 |
| `top_p` | 누적 확률이 p를 초과하는 토큰 집합 (Nucleus Sampling) | 0.85~0.95 |
| `temperature` | 생성 다양성 조절 (낮을수록 보수적) | 0.5~1.0 |

## ⚠️ 주의사항
1. **GPU 환경 권장**: 3090 이상의 GPU에서 4배치 처리 시 약 10분/에폭 소요
2. **데이터 형식**: 반드시 `[UTTERANCE]` 태그로 각 발화 구분 필요
3. **메모리 최적화**: `--fp16` 플래그로 혼합 정밀도 학습 활성화

## 📈 평가 방식
- **Perplexity**: 검증 데이터셋 기준 언어 모델링 성능 평가
- **Human Evaluation**: 생성된 대화의 자연스러움, 일관성, 맥락 이해도 평가

## 📚 참고 문헌
- [Hugging Face Transformers 문서](https://huggingface.co/docs/transformers/)
- [Korean-GPT2 모델 저장소](https://huggingface.co/skt/ko-gpt-trinity-1.5B-v3)
- [Top-k & Nucleus Sampling 논문](https://d4mucfpksyw4.cloudfront.net/arxiv/papers/1904.09751/pdf)

## 🧪 실험 환경
- **하드웨어**: Intel DevCloud GPU 노드
- **소프트웨어**: CUDA 11.6, cuDNN 8.4, TensorFlow 2.9.0

## 📝 라이선스
MIT License (모델 가중치 및 코드)  
데이터셋 사용 시 원본 라이선스 준수 필수

> 💡 **첫 실행 시 주의사항**: 최초 실행 시 모델 다운로드 및 데이터 전처리로 인해 10~30분 추가 소요 가능 (네트워크 환경에 따라 변동)