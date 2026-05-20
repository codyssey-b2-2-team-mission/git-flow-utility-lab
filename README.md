# Git Flow Utility Lab

3인 팀이 GitHub Flow, Issue, PR, Review, Conflict, Troubleshooting을 실습하는 저장소입니다.

## GitHub Flow 선택 이유

- main은 항상 깨지지 않는 기준 브랜치로 둡니다.
- 모든 작업은 `feature/<name>-<topic>` 브랜치에서 진행합니다.
- PR과 리뷰를 거쳐 병합하면 작업 이유와 검증 기록이 남습니다.

## v1 starter gap

현재 v1은 완성본이 아니라 리뷰와 개선 PR을 만들기 위한 starter입니다.

- `normalize_member_name`은 내부 여러 공백을 하나로 줄이지 못합니다.
- `count_words`는 연속 공백을 잘못 셉니다.
- `is_even`은 함수 이름과 다르게 동작합니다.
- 이후 Sangheon Lee, KANGSIK-SEO, giyeop-cody의 PR에서 이 문제들을 순서대로 수정합니다.

## 실행

```sh
python3 src/team_utils.py
```

v1 예상 출력:

```text
normalize_member_name: Sangheon   Lee
member_name_slug: sangheon-lee
count_words: 4
is_even: False
```