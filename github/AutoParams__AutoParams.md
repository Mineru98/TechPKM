---
Language: Java
tags:
 - 테스트 자동 생성
 - JUnit5 확장
 - 테스트 데이터 생성
aliases:
 - AutoParams
 - 테스트 데이터 자동 생성기
 - JUnit5 AutoParams
url: https://github.com/AutoParams/AutoParams
---
AutoParams는 JUnit 5 테스트 메서드 파라미터에 자동 생성된 테스트 데이터를 공급하는 라이브러리입니다. 수동으로 테스트 데이터를 생성하는 번거로움을 줄여 테스트 로직에 집중할 수 있도록 설계되었습니다. `@AutoParams` 어노테이션을 사용하면 파라미터에 랜덤한 값을 자동 주입할 수 있으며, `@Freeze` 또는 `@FreezeBy` 어노테이션을 통해 특정 값의 재사용을 제어하여 복잡한 테스트 시나리오를 효과적으로 구성할 수 있습니다. Lombok, Kotlin, Spring, Mockito와의 통합도 지원하여 다양한 프로젝트에 유연하게 적용 가능합니다.