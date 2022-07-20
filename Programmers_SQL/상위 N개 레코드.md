https://school.programmers.co.kr/learn/courses/30/lessons/59405

상위 N개 레코드
동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요.

```
SELECT Name
from animal_ins
where datetime=(select min(datetime) from animal_ins)
```

출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
