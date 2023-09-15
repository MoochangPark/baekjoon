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
---
### 23년 7월 2일
- [X] 12865 - 냅섹 문제로, 2차원 배열을 만들어서 각 아이템당 한 행을 가진다. 이후 2중 반복을 돌면서 해당 무게와 같은 열이 오기 전까지는 이전 값을 가져오고, 해당 무게와 같은 열에 도달하면 이전 무게를 그대로 쓸지, 아니면 내가 넣을 무게만큼을 빼고 들고있는 무게를 더할건지를 결정하면 된다. 무게를 뺸다고 해도 그 어딘가에 값이 있기 때문에 괜찮다.
- [X] 1916 - 다익스트라로 푸는 문제이지만 끝나는 조건이 있으므로, 이동할 위치를 힙에서 꺼내왔을 떄 끝 조건과 같으면 멈추면 됨
- [X] 1238 - 다익스트라의 경로 탐색을 두 번 진행한다. 첫번째는 목적지까지 가는 것, 두번째는 목적지에서 집으로 오는 것. 다만 두번째인 경우 모든 집에 대해 탐색이 진행되므로 한 번만 진행하고, 첫번째는 시작지점이 전부 달라 반복문으로 각 집마다 다익스트라를 돌려야한다.
---
### 23년 7월 3일
- [X] 10026 - bfs로 쉽게 풀 수 있는 문제이다. 다만 간단하게 풀기 위해서는 색맹이 아닐 경우의 bfs를 한 번 돌리고, 배열의 Red와 Green의 색상을 하나로 통일 한 다음에 다시 한번 bfs를 돌림
- [X] 7569 - 3차원 배열을 [[[0] * m for _ in range(n)] for _ in range(h)] 이렇게 만들어서 bfs를 돌림. 다만 익을 토마토가 없을 떄랑 익을게 있을 때랑 구별해서 먼저 진행하고, 그러고 나서 토마토가 아직 있다면 -1이 처리되도록 하면 됨.
---
### 23년 7월 4일
- [X] 1011 - 수학문제. 이동해야하는 거리를 도착지점 - 시작지점 으로 먼저 구하고, 거리에 따라 이동 패턴을 찾았을 때, (1,2,3,3,4,4,5,5,5,6,6,6)과 같은 패턴이 나오는데, 이를 증감식으로 다시 정리하면 (1,1,2,2,3,3)으로 정리할 수 있다. 결국 2의 배수마다 +1로 증감하기 때문에 증감후 총 값이 기준 거리를 넘지 않는 선에서 계속 카운트를 해주면 된다.
---
### 23년 7월 5일
- [X] 9251 - 두 문자열 중에 하나를 기준으로 잡고 진행. 2차원 배열을 만들어서 만약 비교하는 글자가 같을 때는 양 쪽 다 해당되기 떄문에 i-1, j-1의 위치에서 +1을 함. 비교하는 글자가 다를 경우에는 i-1과 j-1 중에 더 큰 값을 가져옴
---
### 23년 7월 6일
- [X] 15686 - 각 집과 치킨집의 위치들만 기억한 다음 조합을 이용해서 남아있는 치킨집들을 기준으로 치킨거리를 계산
- [X] 1759 - 정렬시킨 알파벳을 DFS를 이용해 순열로 돌면서 조건을 확인하고 출력 
- [X] 1987 - SET, Dictionary, list 모든 상관없지만 알파벳을 그대로 이용하기 보다 "ord(알파벳) - 65"를 활용해서 컴퓨터의 알파벳 변환을 막아주는게 더 중요
---
### 23년 7월 7일
- [X] 14503 - 구현을 하는 문제. 조건에서 후진할 수 있를경우 후진하지만 해당 구문 방문한지 확인해야하는 조건이 없기 때문에 방문 확인에 관한 배열을 조건으로 걸지 않아야 함.
---
### 23년 7월 8일
- [X] 2293 - DP 문제. 어떤 숫자를 만들려고 할 때 해당 동전의 값을 빼고 난 나머지 값을 만들 수 있는 경우의 수를 누적시켜주면서 진행
---
### 23년 7월 9일
- [x] 2839 - 3과 5봉지 뿐이므로 5로 최대한 나눠두고 3으로 나누려고 할때 부족하면 5로 만든 봉지에서 하나씩 가져와서 확인
---
### 23년 7월 10일
- [x] 5430 - 조건 변수를 통해 뒤집혔는지 아닌지를 확인해 뒤에서 값을 뺄지 앞에서 뺄지 결정하며 진행
---
### 23년 7월 11일
- [x] 14500 - 회전 가능과 테트로미노의 가짓수로 인해 4가지 블록으로 만들 수 있는 모든 경우의 수가 가능. ㅗ모양의 경우 dfs나 bfs로 불가능하므로 따로 함수를 만들어서 확인
---
### 23년 7월 12일
- [x] 2206 - bfs로 푸는 문제. 방문 여부를 확인하는 배열에서 벽을 뚫고 온 경우와 아닌 경우를 각각으로 전부 입력받아서 진행. 끝에는 둘 중 한가지 경우로 오기 때문에 마지막 벽 뚫고 왔는지 아닌지의 방문 여부 배열을 출력하면 됨.
- [x] 11054 - 점차 커지는 수열 중에 가장 긴 것과 점차 작아지는 수열 중에 가장 긴 것을 각각 DP로 찾아서 합쳐주기 (LIS 알고리즘)
- [x] 3190 - 리스트의 시작을 꼬리, 끝을 머리로 지정하고 움직이면 됨
---
### 23년 7월 13일
- [x] 11404 - 플로이드-와셜 알고리즘. 2차원배열을 만들어서 출발지와 도착지에 대한 비용을 기록하는데 최단 거리이기 때문에 모두 21E8로 채움. 이후 입력값에서 최소 비용을 우선 저장하고, 플로이드 와셜을 진행한다. 플로이드 와셜은 한 지점을 사이에 두고 직행이 빠른지 아니면 경유가 빠른지를 정하면서 진행한다.
---
### 23년 7월 14일
- [x] 1197 - 가중치가 음수일 경우 플로이드 와셜로 풀 수 없기 때문에 union-find로 문제를 해결할 수 있음
---
### 23년 7월 15일
- [x] 17298 - 스택에 맨 마지막 보다 큰 값이 나올 때까지 쌓음. 이후 더 큰 수가 나올 경우 스택에서 작은 값을 빼가며 값이 있는 인덱스에 지금 발견한 큰 값을 넣음. 이후 히 큰 수를 스택에 저장. 이 순서를 반복함.  
---
### 23년 7월 16일
- [x] 16236 - 구현 문제. 상어의 위치와 먹을 수 있는 물고기 배열 등을 잘 초기화 하는 것이 중요
---
### 23년 7월 17일
- [x] 1107 - 부르트포스  범위가 500,000까지이기 떄문에 1,000,000까지 잡아도 큰 문제가 되지 않는다. 전체 숫자를 돌면서 조건을 비교
---
### 23년 7월 18일
- [x] 2580 - 단순 구현 문제. 다만 dfs 사용시 return은 이전으로 돌아가는 것 뿐이므로 완전히 해당 순간에서 끝내고 싶으면 exit()를 사용해야 함
- [x] 1717 - 유니온-파인드 알고리즘. 이 알고리즘을 쓸 때는 import sys / input = sys.stdin.readline / sys.setrecursionlimit(100000) 을 해야함
- [x] 2252 - 위상정렬 알고리즘. 각 숫자마다 진입 차수를 누적해두고, 각 숫자마다 진출 숫자들을 저장해둔다. 이후 해당 차수가 0이 되면 큐에 저장. 큐에 저장할 때 정답에도 같이 저장함.
- [x] 1916 - 다익스트라 알고리즘. 다만 도착지점이 정해져 있을 경우 heapq에서 꺼내 왔을 때 도착지점에 왔을 경우 멈춰야 함.
- [x] 1806 - 투 포인터 알고리즘. 조건의 n이 100000이므로 answer의 최대 범위를 똑같이 해주어야 한다. 왜냐하면 전체 길이가 정답이 될 수 있기 때문이다
- [x] 13549 - 단순 구현문제. 한칸 뒤, 한칸 앞, 순간이동을 모두 고려해야 하지만 DFS로 하지 않아도 됨. 그리고 순간이동을 되도록 많이 하는게 시간이 짧기 때문에 appendleft를 이용해서 항상 뒤나 앞으로 이동하는 것들보다 먼저 동작하도록 함
- [x] 1504 - 다익스트라 문제. 다만 dictionary를 사용하면 키 에러가 발생할 가능성이 높아 배열로 처리함
- [x] 1715 - 정렬을 해야하는 문제가 아니라면 우선순위 큐인 heapq를 사용해서 작은 값부터 들어오게 만드는 것이 필요
- [x] 1339 - 구현 문제. 숫자의 자리수에 따른 값을 0과 1로 미리 계산해 두는 것이 중요
- [x] 17608 - 스택을 활용해서 가려지는 블록은 뽑아 내버리는게 핵심
- [x] 2493 - 스택을 이용한 구현 문제.
---
### 23년 7월 19일
- [x] 2110 - 이분 탐색 문제. 시작점과 끝 점을 각각 최소거리와 최대거리로 잡아놓고 중간값을 잡음.
---
### 23년 7월 20일
- [x] 14499 - 구현 문제. 주사위의 동서남북 이동을 직접 만들어줄 수 있음
---
### 23년 7월 21일
- [x] 1520 - DP의 bottom_top을 이용해야하는 문제. 해당 위치에서 경우의 수를 구하고, 다른 경로에서 해당 위치로 오게 되면 다시 구할 필요 없이 dp 값을 반환.
---
### 23년 7월 22일
- [x] 16234 - bfs를 사용. 하루 동안 모든 배열을 다 들여다 본 후에 다음날이 진행되야 하므로 while True로 진행하며 조건에 맞춰 멈춰야 함.
---
### 23년 7월 23일
- [x] 1707 - false로 끝내야 할 때는 바로 exit()처리를 하거나 분기 처리를 하자
---
### 23년 7월 24일
- [x] 13460 - 두 구술이 같이 방향으로 이동하게 될 경우 겹치지는 않으므로 해당 경로를 더 길게 움직인 구술이 한칸 뒤로가야 맞음. 그리고 구슬이 이동한 경로는 한 번 더 걸칠 수 있기 때문에 도착지점 모서리들만 기록
---
### 23년 7월 25일
- [x] 2133 - DP 문제. 타일의 경우의 수가 늘어나는 조건을 확인하는게 필요
---
### 23년 7월 26일
- [x] 2294 - dp 문제. 만약 5원을 쓴다면 1부터 k까지 숫자 중 5부터 시작할 수 있고, dp[i-5] + 1 을 해야 5원 하나를 뺐을 때 나오는 최소값 + 5원 하나
가 됨.
---
### 23년 7월 27일
- [x] 2225 - dp 문제. k가 1일때부터 하나씩 2차원으로 계산해보면 바로 알 수 있는 문제
- [x] 12100 - 부르트포스 문제. 숫자를 합치는 방법은 포인트를 하나 만들고 포인트의 위치가 0이면 해당 위치에 숫자를 넣고, 같은 숫자가 있다면 거기에 합친다. 만약 합칠 수 없는 숫자라면 그 뒷 자리에 놓는다.
---
### 23년 7월 28일
- [x] 14891 - deque를 사용하면 rotate를 사용할 수 있으며 기준 톱니의 짝수는 같은 방향, 홀수는 다른 방향으로 회전. 또한 톱니가 돌 때 다 같이 돌기 때문에 돌기 직전 처음 상태들을 가지고 비교
---
### 23년 7월 29일
- [x] 1922 - 최소 스패닝 트리(유니온 파인드 사용됨) 알고리즘 문제. 알고리즘 구현을 잘 하면 끝
---
### 23년 7월 30일
- [x] 2565 - LIS 문제. 범위 내에서 해당 위치보다 낮은 값의 B위치에 연결하면 해당 전깃줄은 삭제 되어야 한다.
---
### 23년 7월 31일
- [x] 1463 - dp문제. 1을 뺼때와 1을 뺀 후에 2나 3으로 나눠지는지 확인하는게 핵심
---
### 23년 8월 01일
- [x] 11047 - 배수이기 떄문에 큰 수에서부터 나눠나가도 좋음.
---
### 23년 8월 02일
- [x] 2573 - bfs 문제. 빙산을 바로 녹이지 않고 기록해 두었다가 bfs가 끝나기 직전에 전부 한꺼번에 녹이는 것이 중요. 또한 bfs가 끝나고 나서도 if 문으로 모아둔 얼음들 위치 중에 바다가 된게 있는지 확인하여 set으로 뺄셈 처리를 해야함.
---
### 23년 8월 03일
- [x] 15683 - dfs을 기반으로 섞은 문제. cctv가 회전할 수 있으므로, 회전했을 때의 경우를 모두 고려해야함. 또한 deepcopy를 이용해서 배열을 넘겨주어야 함.
---
### 23년 8월 04일
- [x] 2751 - 파이썬의 sort는 merge와 합병정렬이 섞여 최적화 되어있음
- [x] 10972 - 수학문제. 큰 수가 뒤에 있을 경우 바꾸는데, 만약 그 뒤에 있는 숫자중에 바꿀게 더 있다면 바꾸고 난 후에 정렬을 한다
- [x] 17144 - bfs문제. 회전할 때 바로 바꾸는게 아니라 하나씩 tmp에 보내고 이전 값을 넣는 식으로 바꾼다.
---
### 23년 8월 05일
- [x] 11050 - 이항계수는 조합이다.
- [x] 19539 - 전체를 더해서 3으로 나눈 몫은 키우는 기간이다. 이떄 각각을 2로 나눈 몫의 총 합이 전체를 3으로 나눈 그 몫보다 작으면 어느 기간중에 한번은 2를 안줬다는 것이므로 해당이 안된다. 혹시 서로 같으면 모든 기간에 알맞게 준 것이고, 2의 몫이 더 많으면 이건 2의 물뿌리개를 1의 물뿌리개를 두 번 준걸로 처리할 수 있어서 괜찮다.
---
### 23년 8월 06일
- [x] 1655 - 두개의 heapq를 사용. 왼쪽으로 모이는 애들은 앞쪽의 작은 애들이 모이게 된다. 또한 - 부호를 달고 오기 때문에 0번쨰를 부르면 자동으로 작은애들 중에 큰 애로 중앙값이 된다.
---
### 23년 8월 07일
- [x] 12015 - 이분탐색 문제. 숫자가 check의 마지막 값보다 크면 넣고, 작을경우 check 중에 바꿀 것이 있나 이분 탐색하여 변경. 왜냐하면 어차피 추후 숫자가 늘어나면 더 작은 애를 넣어주는게 증가하기 쉽기 때문
---
### 23년 8월 08일
- [x] 1967 - dfs 문제. 1번 노드에서 맨 끝 노드들끼리가 우선 가장 길다보니 트리의 최상단 노드는 항상 중앙에 걸치게 될 가능성이 높다. 따라서 1에서부터 먼 곳을 찾고, 찾은 먼 노드에서 또 다시 가장 먼 노드를 찾으면 가장 긴 길이가 된다.
---
### 23년 8월 09일
- [x] 9935 - stack 문제. 일단 문자 하나 넣고 확인할 문자열 길이만큼이 같은지 확인하고 pop을 한다.
---
### 23년 8월 10일
- [x] 1005 - 위상정렬과 DP 문제. 해당 경로로 오기까지 다양한 시작점이 있기 때문에 플로이드 와샬 아니면 위상정렬인데, 해당 지점에 걸쳐지는 다양한 진입들이 전부 끝나야하기 떄문에 위상정렬을 사용. 그리고 경로별로 최대값을 기록하고 활용해야하기 때문에 DP가 적용
- [x] 1167 - dfs 문제. 1967번 문제처럼 중간이 되는 첫번째 노드에서 가장 먼 곳을 찾고, 해당 노드에서 가장 먼 곳을 찾으면 가장 긴 길이가 된다.
- [x] 1644 - 에라토스테네스 채와 투 포인터 문제. 에라토스테네스로 소수를 찾아두고, 투 포인터로 범위를 바꾸어가며 합이 n인지 확인함
- [x] 1918 - stack 문제. (, [*,/], [+,-], ) 총 4가지의 경우에 따라 스택에 있는 값을 뺴내어서 후위식으로 넣어주면 됨
- [x] 3055 - 고슴도치가 움직이면 고슴도치가 갈 수있는 곳을 전부 고슴도치로 표기하고 물이 퍼지는 곳은 전부 물로 표기한다. 대신 확인할 때 내 위치가 고슴도치인지 물인지 확인하면서 움직이는걸로 check 배열을 안해도 됨
---
### 23년 8월 11일
- [x] 2504 - stack문제. 보통은 스택에서 확인만 하지만, 이번 경우에는 곱셈 연산이라서 (()[[]])의 경우 (()) + ([[]]) 와 같음. 따라서 닫는 괄호가 나올 경우 스택에서 아니라 본문에서 직전의 괄호가 자신과 짝인지를 확인하는게 중요
- [x] 9019 - 연산 문제. 숫자를 왼쪽이나 오른쪽으로 한칸 밀 때만 잘 계산해보면 됨. 그리고 이런 문제류는 대부분 DFS로 풀려고 하면 시간초과 남
- [x] 2470 - 투 포인터 문제. 숫자를 우선 정렬하기 때문에 하나의 숫자에서 모든 숫자를 확인할 필요가 없음. 왜냐하면 어차피 오른쪽은 왼쪽으로 와야 점차 숫자가 작아지고, 왼쪽은 점차 오른쪽으로 가야 빼는 값이 적어지기 때문.
- [x] 2096 - DP문제. 메모리초과가 가장 문제라서, 기존의 DP처럼 같은 크기의 배열을 만들고 기록하는게 아니라 한 줄만 쓰면서 전전값은 필요없으니 버림.
- [x] 17070 - DP문제. 하나의 칸에 도달할 때 가로/세로/대각선 중 어디에서 왔는지를 구분하고, 예를 들어 대각선이면, 가로-대각선/세로-대각선/대각선-대각선 중에 어느것인지도 확인해야함.
- [x] 1929 - 에라토스테네스의 채 문제. 범위 설정에 주의
- [x] 11053 - 이분탐색 문제. 12015와 동일한 풀이법
---
### 23년 8월 12일
- [x] 1261 - 다익스트라 문제. 2차원 배열도 결국 그래프와 같기 때문에 시작점과 끝점이 명확하고, 가중치를 일정하게 표현할 수 있다면 다익스트라가 가능
---
### 23년 8월 13일
- [x] 1068 - 트리 문제. 트리라고 해도 꼭 딕셔너리를 만들 필요 없음.
---
### 23년 8월 14일
- [x] 1009 - 수학문제. 1~9까지 제곱들의 끝자리를 보면 패턴이 있다. 해당패턴이 4제곱 단위로 반복되고, 최종 연산 후에 0으로 나눠 떨어지면 10이란 것.
- [x] 14002 - DP문제. 기존의 부분 수열 코드로는 풀 수 없음.
---
### 23년 8월 15일
- [x] 14890 - 경사로 구현 문제. 한 줄에서 i와 i+1을 비교하며 경사로가 올라가는지 혹은 내려가는지 확인. 이때 올라갈 경우 이전의 길이가 조건을 만족하는지 보고, 내려갈 경우 앞으로의 길이가 조건을 만족하는지 확인.
---
### 23년 8월 16일
- [x] 2448 - dfs 문제. 최소 단위인 3일때를 그리는 방법을 생각한 후에 6일때 각 꼭짓점을 기준으로 3일 때의 삼각형을 그리는 패턴을 찾기
---
### 23년 8월 17일
- [x] 2042 - 트리 구간합 문제. 구간합이나 범위의 최대 혹은 최소값을구할때는 트리를 활용하는 것이 좋음.
---
### 23년 8월 18일
- [x] 1032 - 문자열 비교 문제. 문자열 하나를 기준으로 하여 아닌것을 바꾸면 해결.
---
### 23년 8월 19일
- [x] 2636 - BFS 문제. 테두리가 전부 비어있기 때문에 공기와 밀폐된 곳인지 아닌지 확인하지 않고 그냥 돌려도 됨.
---
### 23년 8월 20일
- [x] 1976 - 유니온 파인드 문제. 해당 위치들을 포함한 경로가 있다는 것은 위치들이 같은 집합에 있어야한다는 것을 의미.
---
### 23년 8월 21일
- [x] 2589 - BFS 문제. 돌아가지 않는 최단 거리는 퍼져나가는 도중 겹치는 자리에서 먼저 온 값을 뜻함.
---
### 23년 8월 22일
- [x] 10942 - 펠린드롬 문제. dp로 풀어야하는데, 길이가 1개일때, 2개일때, 3개 이상일때로 나누어서 생각해봐야한다.
---
### 23년 8월 23일
- [x] 5639 - 트리 문제. 전위는 루트-왼쪽-오른쪽 출력하기 때문에 루트와 왼쪽서브트리 오른쪽 서브트리로 잘라가면서 왼쪽 출력 후에 오른쪽 출력하고 루트를 출력하는 방식의 재귀를 수행하면 해결
---
### 23년 8월 24일
- [x] 1300 - 이분 탐색 문제. n*n의 숫자들에서 k번쨰 숫자보다 작은 숫자들만 알면 된다. 이는 k // 행 숫자 로 표현이 가능하며, 이때 k//행의 값이 n을 벗어날 경우 안되는 것이 아니라 n으로 maximum을 설정하면 됨. m번쨰라고 해서 m번쨰에 있을리 없으므로 이를 이분 탐색으로 좁혀나가다 보면 정답에 맞는 mid가 나오게 됨.
---
### 23년 8월 25일
- [x] 9466 - DFS 문제. 그룹의 순환에서 꼭 시작한 사람과 끝 사람이 만나는 순환만 있는게 아니라서, 일단 dfs로 걸치는 사람들을 모두 모으면서 순환이 생겼을 떄 해당 순환 팀을 결과로 반환한다.
---
### 23년 8월 26일
- [x] 9252 - LCS 최장공통부분수열 문제. 기존의 LCS 풀이 방식에 부분 수열들을 저장할 배열을 같이 생성함.
---
### 23년 8월 27일
- [x] 13023 - DFS 문제. 일부가 친구이며 해당 친구들이 5명만 모이면 시작은 누가 하든 상관 없음을 주의.
---
### 23년 8월 28일
- [x] 1202 - 힙 문제. 가장 작은 가방부터 시작하며 가장 크기가 작은 보석부터 넣는다. 다만 가치에 대해서는 최대힙으로 저장한다.
---
### 23년 8월 29일
- [x] 11049 - DP 문제. 2개씩 부터 대각선으로 개수를 늘려가면서 조합의 경우의 수 중에 최소값을 비교하는 것이 중요
---
### 23년 8월 30일
- [x] 11066 - DP 문제. 11049와 비슷하지만 초기 누적합의 값이 있어야 계산이 가능함
---
### 23년 8월 31일
- [x] 1766 - 위상정렬 문제. 순차적으로 풀어야하는 방향그래프이기 떄문에 dfs보단 위상정렬로 풀어야함.
---
### 23년 9월 1일
- [x] 15685 - 구현 문제. 구현시에 문제 자체에 패턴이 있다면 패턴을 찾아야함
---
### 23년 9월 2일
- [x] 10830 - 분할정복 문제. 분할정보글 위해 재귀를 호출할 떄 가능하다면 재귀할 함수호출을 한번만 해도 되는지 확인하는게 필
---
### 23년 9월 3일
- [x] 프로그래머스 sql
---
### 23년 9월 4일
- [x] 13913 - bfs 문제. 체크 배열을 만들어서 내가 이미 갔던 곳은 반복되기 떄문에 더 갈 필요가 없으며, deque에서 뽑은 list는 append가 안되므로 리스트+리스트 를 사용해야 한다.
---
### 23년 9월 5일
- [x] 7662 - heapq문제. 최대 힙과 최소 힙을 둘 다 사용해야하기 때문에 명령을 수행하기 전에 서로 각자 뺸 것을 항상 check 배열을 통해 확인해서 다 뺴줘야한다.
---
### 23년 9월 6일
- [x] 2146 - bfs문제. 땅의 테두리만 알 필요 없이 해당 땅의 시작을 전부 0으로 두고, 다음 위치가 땅일 경우 q에 안 넣으면 됨.
---
### 23년 9월 7일
- [x] 1744 - 그리디 문제. 양수끼리 음수끼리 계산해야 하므로 두가지로 나눠서 두 번 반복하면 해결.
---
### 23년 9월 8일
- [x] 1037 - 정렬 문제. 정렬 후 양 끝 값을 곱하면 됨.
---
### 23년 9월 9일
- [x] 1075 - 브루트포스로 00에서부터 1씩 더해가면서 나눠지는지 확인.
---
### 23년 9월 10일
- [x] 12851 - bfs문제. 똑같은 경우의 수를 한칸씩으로 가거나 점프로 갈 수 있어 횟수로 체크해야함
---
### 23년 9월 11일
- [x] 1937 - dfs 문제. 모든 위치에 대해 dfs를 돌리는데, 갈 수 있는 최대치까지 가서 거기서부터 1씩 더해가며 이전 경로들을 갱신한다. 그러다보면 시작점은 이전 경로가 더 긴지, 새롭게 다녀온 경로가 더 긴지 확인할 수 있다.
---
### 23년 9월 12일
- [x] 16928 - bfs 문제. 계단, 뱀, 빈칸 중에 무엇인지를 잘 확인해야하는데, 이때 각각을 if-elif-else가 아닌 3개의 if로 처리해야한다.
---
### 23년 9월 13일
- [x] 9205 - bfs 문제. 20개를 카운트 할 필요 없이 두 점 사이의 거리가 맥주를 마시며 갈 수 있는 최대 거리안에 있기만 하면 된다.
---
### 23년 9월 14일
- [x] 4485 - 다익스트라 문제. 2차원 배열에서 상하좌우가 다음 노드이고, 위치들의 숫자를 가중치로 함. 목적지가 정해져있어 dfs도 가능하지만 다익스트라여도 가능
---
### 23년 9월 15일
- [x] 1043 - 유니온 파인드 문제. 진실을 알고 있는 사람끼리 그룹을 짓는 과정을 모두 수행한 후에 하나의 파티씩 돌면서 다시 체크하는게 중요
