# Git Flow Utility Lab

3인 팀이 GitHub Flow, Issue, PR, Review, Conflict, Troubleshooting을 실습하는 저장소입니다.

## GitHub Flow 선택 이유

- main은 항상 깨지지 않는 기준 브랜치로 둡니다.
- 모든 작업은 `feature/<name>-<topic>` 브랜치에서 진행합니다.
- PR과 리뷰를 거쳐 병합하면 작업 이유와 검증 기록이 남습니다.

## Starter 개선 기록

- Sangheon Lee PR 2: `normalize_member_name`이 내부 여러 공백을 하나로 정리하도록 수정했습니다.
- KANGSIK-SEO PR 1: `count_words`가 연속 공백과 공백 문자열을 자연스럽게 처리하도록 수정했습니다.
- giyeop-cody PR 1: `is_even`이 짝수일 때 `True`, 홀수일 때 `False`를 반환하도록 수정했습니다.

## 실행

```sh
python3 src/team_utils.py
```

최종 예상 출력:

```text
normalize_member_name: Sangheon Lee
member_name_slug: sangheon-lee
count_words: 3
is_even: True
```

## 추가 확인 예시

```text
normalize_member_name("  sangheon   lee ") == "Sangheon Lee"
member_name_slug("  sangheon   lee ") == "sangheon-lee"
count_words("Git  flow utility") == 3
count_words("   ") == 0
is_even(4) == True
is_even(5) == False
```
