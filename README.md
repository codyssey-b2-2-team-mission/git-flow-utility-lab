# Git Flow Utility Lab

3인 팀이 GitHub Flow, Issue, PR, Review, Conflict, Troubleshooting을 실습하는 저장소입니다.

## GitHub Flow 선택 이유

- main은 항상 깨지지 않는 기준 브랜치로 둡니다.
- 모든 작업은 `feature/<name>-<topic>` 브랜치에서 진행합니다.
- PR과 리뷰를 거쳐 병합하면 작업 이유와 검증 기록이 남습니다.

## Current status

Sangheon Lee PR에서 이름 정규화 문제를 수정했습니다.
이번 PR에서는 `count_words`, `is_even`의 남은 starter gap은 수정하지 않고 후속 PR에 남깁니다.

남은 starter gap:

- `count_words`는 아직 연속 공백을 잘못 셉니다.
- `is_even`은 아직 함수 이름과 다르게 동작합니다.

## 실행

```sh
python3 src/team_utils.py
```

현재 예상 출력:

```text
normalize_member_name: Sangheon Lee
member_name_slug: sangheon-lee
count_words: 4
is_even: False
```