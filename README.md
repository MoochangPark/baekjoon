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
---
### 23년 6월 17일
- [X] 1158 - 배열을 시작할 떄 do while을 사용할 것이 아니라면 -1부터 위치를 시작하면서 진행
---
### 23년 6월 18일
- [X] 1166 - 범위가 크지만 DP가 안될 떄는 이분 탐색을 고려, 범위를 지정하고 가로/세로/높이별 만들 수 있는 개수를 곱해 확인
---
### 23년 6월 19일
- [X] 1181 - lambda를 이용해서 sort를 하는 것이 핵심
---
### 23년 6월 20일
- [X] 1182 - 백트래킹, 즉 check 배열을 만들어서 경우의 수를 할 수 도 있지만, yes/no의 이진분법으로 해결 가능
---
### 23년 6월 21일
- [X] 1183 - 최소 시간을 구한 후에 정렬 하면 범위가 나오는데, 홀수는 각 숫자가 다 달라 1개가 최대지만, 짝수의 경우 중간 범위가 개수가 되므로 해당 개수를 구하기 위해서는 중간 범위를 찾아주면 끝
---
### 23년 6월 22일
- [X] 1189 - 도착 지점이 r, c일 경우 배열에서는 r-1, c-1이 되어야 함
---
### 23년 6월 23일
- [X] 1198 - |(x1y2 + x2y3 +x3y1) - (x2y1 + x3y2 + x1y3)| / 2 이라는 가우스의 면적 공식을 통한 삼각형 넓이 구하기
---
### 23년 6월 24일
- [X] 1205 - 같은 점수일 경우 내 점수와 같은 점수면 안 올려도 되고, 다른 점수면 누적시켜야 함
---
### 23년 6월 25일
- [X] 1213 - 홀수 짝수로 나누어서 문자열을 생성하고 나중에 합침
---
### 23년 6월 26일
- [X] 7576 - 토마토 마다 익은 시간대를 기록하고 활용하는 것이 중요
- [X] 9663 - n 만큼 길이의 배열을 만들고 배열의 열을 행, 값을 열로 잡는다. 그리고 각 행마다 퀸이 하나씩 놓을 수 있으므로 행 단위로 dfs를 도는데, 해당 행에서 퀸을 각 열마다 놓으면서 같은 열어 다른 퀸이 있거나 대각선에 있는지 확인한다.
---
### 23년 6월 27일
- [X] 2447 - 재귀에서 작은 단위의 결과물(배열)을 return하여 해당 패턴을 반복하는 방식도 있다.
---
### 23년 6월 28일
- [X] 11653 - 모든 값들을 나눠봐서 나눠 떨어질 경우 출력
---
### 23년 6월 29일
- [X] 1235 - 배열이나 문자열의 역순 출력은 list[-i : ]로 하면 for문 돌때 0부터 할 수 있음
---
### 23년 6월 30일
- [X] 14502 - 벽을 세울 수 있는 모든 경우의 수를 기준으로 bfs를 돌려 확인
---
### 23년 7월 1일
- [X] 1753 - 다익스트라는 값을 전부 딕셔너리로 받고, heapq를 사용해서 하나씩 꺼내가면서 갈 수 있는 길 중에 가장 가중치가 작은 애를 기록하면서 움직인다. 이때 조건이 성립할때마다 가중치 리스트에 기록하면 갈 수 있는 다른 길이 이전 기록값을 가지고 비교하기 때문에 문제가 되지 않으며, 가중치 리스트는 처음부터 21E8로 만들어둬서 시작 지점에서 갈 수 없는 경로는 아무리 계산해도 21E8보다 커질 수 밖에 없기 때문에 문제 없음 
- [X] 17244 - 시작, 아이템, 끝에 대한 위치들을 기록하고, 각각에 대한 방향그래프를 BFS 돌리며 matrix로 작성한다. 후에 방향그래프를 가지고 완전탐색을 위한 DFS를 돌리면서 시작지점에서부터 아이템을 다 먹고 나가는 경우의 수 중에서 가장 짧은 거리를 구한다.
