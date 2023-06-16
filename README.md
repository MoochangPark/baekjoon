# Baekjoon 문제 풀이에서 기억해야할 점

### 23년 6월 12일
- [X] 1002 - 좌표 거리 및 원과 원의 관계
- [X] 1003 - 배열을 통해 0과 1의 증가 값을 누적
- [X] 1004 - 출발점과 도착점 각각의 행성 중점 사이 거리 측정 후 행성 범위 내 인지 확인 (시작과 끝이 행성 안에 있으면 패스)
- [X] 1010 - 경우의 수 (조합)
- [X] 1012 - 8방향이 아니므로 bfs로 배추를 점령
- [X] 1015 - 작은 숫자 부터 어느 숫자가 인덱스가 더 작은지 정렬
---
### 23년 6월 13일
- [X] 1018 - 시작이 W인지 B인지 확인하지 않고, 시작 지점의 색깔을 두 가지 전부로 가정하며 체크
- [X] 1021 - 절반을 기준으로 왼쪽으로 갈지 오른쪽으로 갈지 결정
- [X] 1026 - B를 건들면 안된다고 했지만 해도 문제되지 않음
- [X] 1049 - 모든 경우의 수를 고려해 팩 / 단일 / 팩 + 단일 의 경우를 확인
- [X] 1051 - 갈수 있는 범위를 줄이기 보다는 범위를 넘어서는지 확인하는 것이 쉬움
---
### 23년 6월 14일
- [X] 1052 - 합쳐가면서 더하는게 아니라 일단 합칠 수 있는 만큼 합쳐두고 추가하기 (binary 활용)
- [X] 1057 - 라운드에 따라 각자의 순서가 얼만큼 줄어드는지 확인
- [X] 1059 - 최소와 최대의 범위를 잘 정하기
- [X] 1063 - 킹이 움직이려는 방향에 돌이 있을 경우 돌도 같이 움직일 수 있는지 확인
- [X] 1065 - 문자열의 분리하는 법
---
### 23년 6월 15일
- [X] 1072 - 반복문의 범위가 클 경우 정렬에 따라 이분탐색이 가능한지 여부 확인
- [X] 1074 - 4분면일 때는 한 면씩 확인하는게 좋으며, 범위를 좁힌 후에는 범위에 맞게 좌표를 재 조정하는게 필요
- [X] 1080 - 순서는 상관없이 순차적으로 뒤집는 것이 핵심
- [X] 1094 - 절반씩 줄어든다는 부분에서 이진수를 의심
- [X] 1105 - 숫자가 같은 경우는 두 숫자가 8인 경우와 같으면서도 해당 범위가 변동이 없으므로 else로 처리되면 안됨
---
### 23년 6월 16일
- [X] 1120 - 비교를 위해서 가장 길이가 작은 쪽을 중심으로 잡기
- [X] 1124 - DP를 활용할 수 있도록 하되, 각 수에 대한 소수 누적은 2중 반복문을 통해 해결한다. 단 숫자가 큰 것부터 분류해야하기 떄문에 반복문을 통해 이전에 값(ex. 6은 소수 2로 인해 2개가 되었지만 소수 3으로 인해 2개로 덮어 씌워진 것 처럼)이 덮어져도 문제가 없다
- [X] 1138 - 몇 번째에 빈자리를 건너가야 하는지 계산하면 되는데, 다만 이미 작은 숫자부터 채워지기 떄문에 이미 채워진 자리들은 고려하지 않아도 됨
- [X] 1141 - 가장 짧은 길이부터 시작해서 아닐 경우 전체 개수에서 차감하는 방식으로 진행
- [X] 1149 - DP로서 이전에 집값 중에 가장 싼 값을 누적해 나감(시작을 무엇으로 할지가 중요하기 때문에 빨, 파, 초 전부 확인해야함)
