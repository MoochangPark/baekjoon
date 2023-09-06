# mySQL 문제 풀이에서 기억해야할 점
---
### 23년 9월 3일
- [X] 59035 - 순차는 ASC, 역순은 DESC
- [X] 59036 - 조건을 찾을 떄는 WHERE 부터
- [X] 59403 - 정렬할 때는 ORDER BY를 써준 후 ASC/DESC 사용
---
### 23년 9월 4일
- [X] 59405 - 갯수 제한은 LIMIT
- [X] 59037 - WHERE에서 같지 않은 것은 !=
- [X] 59407 - WHERE 다음에 ORDER BY 사용
- [X] 131528 - 갯수 세는건 COUNT, 컬럼명 변경은 AS, NULL인지 확인은 IS NULL
- [X] 59404 - ORDER BY에서 여러개 적용 가능, 각 조건마다 ASC와 DESC 적용 가능 (EX. NAME ASC, ID DESC)
- [X] 131697 - 최대 값은 MAX
- [X] 131114 - 표기 내용을 바꾸는 것은 SELECT에서 IF 사용, 내용에 조건이 들어있는지 확인은 WHERE과 LIKE (%는 여러개, _는 한개)
- [X] 59039 - 131528의 IS NULL과 방법이 같음
- [X] 131112 - 131114의 LIKE와 방법이 같음
- [X] 131535 - WHERE 조건이 여러개 일 떄는 AND를 사용
- [X] 132203 - 날짜 형식 지정은 DATE_FORMAT(HIRE_YMD,"%Y-%m-%d"), 같다는 =, 같지않다는 !=, ORDER BY 작성 순서에 따라 순차적 비교
- [X] 132201 - SELECT에서 IF사용할 때 AS 사용하기
- [X] 133024 - 59404의 여러개 지정과 같음
- [X] 144853 - 132203과 같이 DATE_FORMAT 사용, 사용할 떄 AS로 바꿔주는게 필요
- [X] 151136 - 평균은 AVG, 반올림은 ROUND, 올림은 CEIL, 내림은 FLOOR, 중첩 가능(EX. ROUND(AVG())
- [X] 59034 - SELECT에서 모든 선택은 *
- [X] 133025 - JOIN 사용법 ( SELECT A.FLAVOR FROM FIRST_HALF AS A LEFT JOIN ICECREAM_INFO AS B ON A.FLAVOR = B.FLAVOR )
- [X] 59415 - 59405의 LIMIT과 같은 방법
- [X] 157343 - LIKE 사용할 떄 중간에 포함되는 내용이면 %를 양 옆으로 붙임 (EX. %네비게이션%)
- [X] 151138 - 날짜 계산은 IF 안에서 DATEDIFF 사용
- [X] 164673 - JOIN 중에서 필요한 경우 INNER JOIN 사용
---
### 23년 9월 5일
- [X] 59047 - 여러개의 조건은 AND
- [X] 59410 - IF 조건을 사용할때 NULL인지 확인할 떄는 IS NULL
- [X] 59414 - 날짜 형식 바꿀 떄는 DATE_FORMAT
- [X] 131115 - 제일 높은 값 하나를 원할 떄는 LIMIT 혹은 조건에 () 사용 (EX. WHERE PRICE = (SELECT MAX(PRICE) FROM TABLE))
- [X] 59409 - IF에서도 OR로 조건 여러개 가능 (EX. IF(SEX_UPON_INTAKE LIKE "%Neutered%" OR SEX_UPON_INTAKE LIKE "%Spayed%", "O", "X")) 혹은 CASE로 처리 (EX. CASE WHEN SEX_UPON_INTAKE LIKE 'Neutered%' OR SEX_UPON_INTAKE LIKE 'Spayed%' THEN 'O' 
 ELSE 'X' END 중성화 )
- [X] 131529 - 별칭으로 지어진 컬럼도 GROUP BY 사용 가능
- [X] 132202 - ORDER BY 에서도 COUNT 같은 것을 사용할 수 있음
- [X] 131533 - 중복 제거 없이 합칠떄는 그냥 JOIN 을 사용. 대신 한쪽 테이블에서 필요한 것만 SELECT로 따로 뺴와야함. JOIN 후에 GROUP BY로 갯수 카운트가 가능.
- [X] 151137 - WHERE에서 여러개 조건 사용 가능
- [X] 144854 - 간단한 JOIN은 INNER JOIN
- [X] 59046 - WHERE에서 간단하게 IN으로 처리 가능 (EX. NAME IN ("A", "B", "C", "D") )
- [X] 133026 - GROUP BY 이후에 SUM이 사용됨
- [X] 131530 - TRUNCATE는 소수점의 자리를 버릴 수 있지만 -를 사용하면 앞 자리도 버릴 수 있음
- [X] 131120 - 년/월/일 중에 하나만 필요하면 MONTH 등을 사용 가능
- [X] 131536 - 같은 테이블에서 중복체크할 떄는 JOIN이 아닌 GROUP BY에서 조건들을 전부 넣고 HAVING으로 COUNT(*) >= 2 조건을 걸어 처리해도 됨.
- [X] 164672 - CASE와 WHEN~THEN, END 로 IF보다 여러 조건 처리 가능
- [X] 157342 - DATEDIFF를 사용하면 항상 +1을 해주고, GROUP BY로 묶을 때 조건은 HAVING으로 처리
---
### 23년 9월 6일
- [X] 59044 - 교집합을 뺴려면 WHERE B.ID IS NULL 이라는 조건을 붙여야 함
- [X] 59043 - 기간을 구하는게 아닌 단순 날짜 비교는 부등호를 사용해도 됨.
- [X] 59411 - 교집합은 그냥 JOIN을 하면 됨.
- [X] 144855 - JOIN 할 때 WHERE 조건을 걸어버린 후 GROUP BY 사용
- [X] 131113 - 조건 분류는 CASE
- [X] 164668 - JOIN 후에 WHERE 조건으로 한번 거르고, 나머지 조건을 GROUP BY와 HAVING으로 처리
- [X] 131123 - 조건 안에 조건이 있을 경우 WHERE (A, B) IN (SELECT A, MAX(B) FROM TABLE GROUP BY A) 방식의 IN을 사용해야 함
- [X] 157341 - 결과의 중복 제거는 DISTINCT
- [X] 59042 - 이름은 겹칠 수 있어 정확한 ID로 검색
