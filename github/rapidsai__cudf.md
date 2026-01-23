---
Language: Python/CUDA C++
tags:
 - GPU 데이터 처리
 - Apache Arrow 호환
 - pandas 연동
 - Polars 연동
 - Dask 연동
aliases:
 - cuDF
 - RAPIDS cuDF
 - GPU 가속 DataFrame
 - cudf 라이브러리
 - Velox-cuDF 연동
url: https://github.com/rapidsai/cudf
---
cuDF는 GPU 가속 기반의 Apache 2.0 라이선스 DataFrame 라이브러리로, RAPIDS 에코시스템의 핵심 구성 요소입니다. 표 형식 데이터를 고속으로 처리하기 위해 설계되었으며, pandas API와 호환되는 Python 인터페이스와 Apache Arrow 호환 C++ 라이브러리를 제공합니다. Spark RAPIDS, Velox 확장 모듈 등 주요 프로젝트에서 활용되며, CUDA 12/13 환경에서 pip 또는 conda를 통해 설치 가능합니다.  

cuDF는 `cudf.pandas` 모듈을 통해 기존 pandas 코드를 수정 없이 GPU 가속할 수 있으며, Polars와 Dask와의 통합을 지원합니다. 설치 후 `import cudf` 또는 `%load_ext cudf.pandas`를 통해 즉시 사용 가능합니다.