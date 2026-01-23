---
Language: Python/C++
tags:
 - GPU 가속
 - 데이터 분석
 - DataFrame
 - RAPIDS
 - CUDA
aliases:
 - cuDF
 - GPU DataFrame
 - RAPIDS cuDF
 - GPU 가속 데이터 처리
 - cudf pandas
url: https://github.com/rapidsai/cudf/blob/main/README.md
---
cuDF는 GPU 가속을 지원하는 Apache 2.0 라이선스 DataFrame 라이브러리로, RAPIDS 데이터 과학 스위트의 핵심 구성 요소입니다. pandas와 유사한 API를 제공하면서도 GPU를 활용하여 대용량 테이블 데이터 처리 성능을 극대화하며, Dask 및 Polars와의 통합을 지원합니다. 주요 구성 요소로는 C++ 기반 libcudf, Python 바인딩 pylibcudf, 그리고 pandas/Dask/Plars용 GPU 엔진이 포함됩니다.  

cuDF는 Spark RAPIDS, Velox-cuDF 등 다양한 프로젝트에서 활용되며, pip/conda를 통해 CUDA 버전에 맞춰 설치 가능합니다. 기존 pandas 코드를 변경 없이 GPU로 가속화하는 `cudf.pandas` 기능도 제공합니다.