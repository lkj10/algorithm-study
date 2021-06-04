# Algorithm Study

### 남은 기간 열심히 해서 좋은 성과 얻어요 ~~!!

## 💖 1. What

`Baekjoon`, `Programmers` `leetcode` 등에서 Baekjoon 기준 from 실버 to 골드인 문제를 선별해서 풉니다. 

<h4>
    <a href="https://www.notion.so/ca0b8a585bf945a69ae852058ff69773">
        😎 이번 주 풀어야할 문제 보러가기
    </a>
</h4>
<h4>
    <a href="https://www.notion.so/23e643615b494706b7ddcf1bf0b055ff"> 
        😗 풀고 싶은 문제 추천하러 가기 
    </a>
</h4>
<h4>
    <a href="https://www.notion.so/07e03c54c65d4753822f93f860d02ec6?v=6f341b068d0c499db287871823708e35"> 
        😗 건의 하러 가기 ~~
    </a>
</h4>

## 😈 2.  How

  `Pull Request`로 자신이 푼 문제를 제출 해요.

- 매 주 돌아가며 한 명씩 내고 싶은 문제 추려 내 제출하기
- 화요일 3문제 목요일 2문제
- 화요일에 전체 오프라인 리뷰하기
- 목요일 줌, 행 아웃을 통한 온라인 실시간 리뷰하기
- 공부 더 하고 싶을 때 주저하지 말고 얘기해서 모여서 각자 코딩하기 (줌 활용)

## 🐶 3. Convention
저희는 다음과 같은 Convention을 지키는 걸 지향합니다

### ✅  Code Convention

#### 코드 마다 이 코드는 `어떤 목적` 으로 작성되었는지 주석을 답니다.
#### 변수와 함수 이름은 어떤 역할을 하는지 알 수 있도록 붙입니다.

> 목적과, 변수 함수의 이름 등이 어떠한 역할을 하는 지 고민해봐요
  
### ✅ Commit Convention

#### 한 번에 git add . 하는 것보다 commit type에 맞게 분리하는 걸 지향합니다.
```
docs : README.md 등 문서 작성 및 수정
feat : 코드 작성
fix : 코드 수정
add : 기존에 푼 문제 대한 또 다른 솔루션 코드 추가
```
commit type 'code'인 경우 commit message에는 다음과 같은 정보를 명시하는 걸 지향합니다.
```
git commit -m "feat : 몇주차 문제플랫폼 문제번호 문제유형 문제이름"  
```

**예시는 다음과 같습니다.**

펭수라는 사람이 있습니다. 펭수의 github ID는 pengsu2입니다. 펭수는 프로그래머스에서 기능개발 문제를 풀었습니다.

우선 코드를 하나의 커밋으로 분리합니다.
```bash
git add progresses.py
git commit -m "feat : 4weeks programmers progresses solved"
```

> 깃허브 데스크탑 또는 IDE 자체 터미널을 쓰시는 경우는 파일 **하나씩** 스테이징 해주시고, 커밋 컨벤션 지켜주시면 됩니다.

### ✅ Review Convention

#### Pull Request 를 작성할 때 제목에는 ""을 작성하는 것을 지향합니다.
```
4weeks all solved
```

```
4weeks progresses solved, 미로찾기 ing
```

#### 자신이 푼 문제 유형을 자신의 pull request에 label을 붙입니다.

#### 라벨은 직접 만들어서 사용하면 됩니다. `ex) Brute-Force, DFS, BFS`

#### 자신의 pull request의 `assignee`에 자신을 추가합니다.

#### 자신이 받고 싶은 review 받고 싶은 `reviewer`가 있을 경우, 자신의 pull request에 `reviewer`로 추가합니다.

#### 기존에 Pull Request를 작성했지만 새로운 문제를 풀었을 경우, 새로운 문제에 대한 commit을 하기 전 다음과 같은 과정을 수행하는 것을 지향합니다.

---
<br>

**상황1. 자신의 PR에 대한 적절한 리뷰를 받았다고 생각했을 경우,**

1. 해당 오가니제이션의 레포의 **github issue**에 자기가 푼 문제에 대한 issue를 생성합니다. 이슈 제목에는 "본인 이름: 문제 플랫폼 문제유형 문제이름" 또는 "본인 이름: 문제 플랫폼 문제 번호 문제 유형 문제이름"을 작성하는 것을 지향합니다.

```
윤장원 : programmers stack 기능개발
```

```
윤장원 : boj 2160 BFS, DFS 미로 찾기
```

2. 자신이 작성했던 Pull Request에서 초록색 `merge`버튼을 눌러서 `merge`합니다.

3. 자신이 작성했던 Pull Request에서 issue로 앞서 생성한 이슈를 연결합니다. 이슈는 닫히지 않았는지 확인합니다.


> 위 과정에 이해가 안되는 부분은 연락 해주세요~~ 