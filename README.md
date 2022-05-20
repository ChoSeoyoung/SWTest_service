# Django 실습 : [Django를 이용하여 시험지 만들기]

## 프로젝트 개요
### 프로젝트 소개
끊임없는 학습을 요구하는 시대에 발맞춰, 자기주도 학습의 중요성이 대두되고 있다. 해당 프로젝트를 통해서 소개할 시험지 만들기 서비스는 자기주도 학습의 효율을 높일 수 있는 좋은 방법이 될 수 있다. 기존의 학습법인 노트에 중요 문제를 직접 필기해가며 공부하는 방식은 필기를 잃어버리거나, 답안을 반복해서 풀기 어려웠던 문제점들이 존재했다. 하지만 해당 서비스를 이러한 문제를 극복할 수 있을 뿐만 아니라, 통계 기능을 통해 답안의 분포까지 확인할 수 있다. 본 프로젝트는 학생들의 자기주도학습을 도울 “Django 실습: 시험지 만들기”를 주제로 한다.

### 개발 목표
1. 기본적인 CRUD기능
	- CREATE: 문제출제 기능
	- READ: 문제상세 기능
	- UPDATE: 문제수정 기능
	- DELETE: 문제삭제 기능
2. 추가기능
	- 응시하기
	- 통계보기
<br>

## 시스템 기능
### 화면 설계
![image](https://user-images.githubusercontent.com/74875490/169581536-5b5a4a01-0e66-4ac1-8952-144314a0875e.png)

### API 설계
![image](https://user-images.githubusercontent.com/74875490/169579714-d84ca816-4dd6-4fcb-80ac-30d73302f2a9.png)
<br>

## 시스템 구현
1. 메인 메뉴
![image](https://user-images.githubusercontent.com/74875490/169573183-9eed2f9a-0d5a-4692-8307-32a4e4fedf4a.png)<br>
웹 사이트의 메인 화면이다.

2. 문제 목록
![image](https://user-images.githubusercontent.com/74875490/169573521-40f9a65a-81d2-4654-aeea-ad6631ca58d1.png)<br>
등록한 모든 문제가 표시된다.

3. 문제 등록(출제하기)
![image](https://user-images.githubusercontent.com/74875490/169573798-071f0270-a10e-497e-a621-e553345bddcd.png)<br>
문제 등록 폼 작성을 통해서 문제를 등록할 수 있다. “등록” 버튼을 누르면 문제가 새로이 등록된다.

4. 문제 상세
![image](https://user-images.githubusercontent.com/74875490/169574136-bcf795c1-5586-45fc-8d65-9d649611e853.png)<br>
등록한 문제에 대한 상세 정보가 표시된다.

5. 문제 수정
![image](https://user-images.githubusercontent.com/74875490/169582626-72f736ac-997d-4a00-8953-a33b2fee03de.png)<br>
문제 등록 화면과 마찬가지로 폼 입력을 통해 기존의 문제를 수정할 수 있다.

6. 문제 응시
![image](https://user-images.githubusercontent.com/74875490/169574490-0b081824-76b5-4d46-90c0-aa7db2823649.png)<br>
문제 응시 화면에서 다음과 같이 4지선다형 문제를 풀 수 있다. 구현은 라디오 버튼으로 구현했으며, “제출” 버튼을 누르면 정답을 확인할 수 있다.

7. 응시 결과(통계)
- 정답인 경우 
![image](https://user-images.githubusercontent.com/74875490/169575653-7c605a3b-0ccf-4a3d-bb58-06f86d664c8a.png)
![image](https://user-images.githubusercontent.com/74875490/169576256-cf820aa8-7b58-4309-bb7a-19ec45e2a2c8.png)<br>

- 오답인 경우
![image](https://user-images.githubusercontent.com/74875490/169576460-29af8a9d-fd07-4f1d-a9f4-dceb95a1426d.png)
![image](https://user-images.githubusercontent.com/74875490/169576555-412575a2-8321-4d41-b48c-77ec795e5683.png)<br>
답안이 맞았을 경우에는, “맞았습니다.” 팝업 알림과 함께 통계 결과가 보여진다. 하지만, 답안이 틀렸을 경우, “틀렸습니다.” 팝업 알림과 함께 통계 결과, 그리고 정답, 오답이 함께 보여진다.