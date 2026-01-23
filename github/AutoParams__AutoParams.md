---
Language: Java  
tags:  
 - 테스트 데이터 생성  
 - JUnit 확장  
 - AutoFixture  
 - 테스트 자동화  
 - 파라미터 생성  
aliases:  
 - AutoParams  
 - AutoParams-JUnit  
 - AutoFixture-Java  
url: https://github.com/AutoParams/AutoParams  
---  
**AutoParams**는 JUnit 5 확장 기능으로, 테스트 데이터 생성을 자동화하는 라이브러리입니다. AutoFixture에서 영감을 받아 반복적인 테스트 데이터 준비 작업을 제거하여 테스트 로직에 집중할 수 있도록 설계되었습니다. `@AutoParams` 어노테이션을 사용하면 테스트 메서드 파라미터에 자동으로 생성된 값을 주입할 수 있습니다. 또한 `@Freeze` 어노테이션이나 커스터마이징 기능을 통해 복잡한 테스트 시나리오도 지원하며, 컬렉션 생성, 값 범위 지정, 커스텀 생성기 적용 등의 고급 기능을 제공합니다. Lombok, Spring, Mockito, Kotlin과의 통합도 지원합니다.  

**핵심 기능**  
- 자동 파라미터 생성 (`@AutoParams`)  
- 공유 값 고정 (`@Freeze`, `@FreezeBy`)  
- 값 범위 지정 (`@Min`, `@Max`)  
- 커스텀 생성기 및 DSL 기반 일회성 커스터마이징  
- 컬렉션 및 배열 생성  
- Lombok 빌더/Lombok 어노테이션 지원  
- Spring 빈 통합 (`@UseBeans`)  
- Mockito 테스트 더블 생성  
- Kotlin 데이터 클래스 지원 (`@AutoKotlinParams`)  

**장점**  
- 테스트 코드 간결화  
- 반복 작업 감소  
- 복잡한 테스트 시나리오 관리 용이  
- 다양한 기술 스택과의 호환성  

JDK 1.8 이상에서 사용 가능하며, Maven 또는 Gradle을 통해 쉽게 설치할 수 있습니다.