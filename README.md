# Git Flow Utility Lab


<!-- codyssey-links:start -->
## 🔗 Codyssey 연결

| 항목 | 링크 |
|---|---|
| **과제** | **B2-2** — 친구 3~5명과 함께 프로그램 만드는 법 연습하기 · 기초(Basic) 「AI/SW 기초」 · Python과 Git 심화 · 20h |
| 미션 원문 (정의서) | [`B2-2/b2-2-description.md`](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B2-2/b2-2-description.md) · [`B2-2-mission.jpg`](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B2-2/b2-2-mission.jpg) · [`meta.json`](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B2-2/meta.json) |
| 이 과제 연결 카드 | [`B2-2/links.md`](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B2-2/links.md) |
| 전체 연결 대장 | [`LINKS.md`](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/LINKS.md) · 진행 현황 [`PROGRESS.md`](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/PROGRESS.md) · [원문 API URL 41개](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/codyssey-all-urls.md) |
| 과정 허브 | [ai-sw-basic](https://github.com/giyeop-cody/ai-sw-basic) `/B2-2/` 서브모듈 |
| 통합 레포 | [codyssey](https://github.com/giyeop-cody/codyssey) → `ai-sw-basic/B2-2/` |
| 다음 과정 | 심화(A) [codyssey-A-studylog-hub](https://github.com/giyeop-cody/codyssey-A-studylog-hub) · 응용(M) 정의서 [`taskmap/M*/`](https://github.com/giyeop-cody/codyssey-taskmap/tree/main/M1-1) |
| 같은 과제의 다른 레포 | <sub>선행/개인</sub> [giyeop-cody/B2-2](https://github.com/giyeop-cody/B2-2) |
| 같은 과목 다른 과제 | [B2-1](https://github.com/giyeop-cody/codyssey-taskmap/blob/main/B2-1/links.md) |

> 🔒 = 비공개 레포. 상태·pin 커밋은 연결 카드와 `PROGRESS.md` 에 있다. 이 표는 2026-09-27 기준이며 미션 원문 3종은 원본 데이터라 진행 상태를 쓰지 않는다.
<!-- codyssey-links:end -->

3인 팀이 GitHub Flow, Issue, PR, Review, Conflict, Troubleshooting 흐름을 실습하는 저장소입니다.

## GitHub Flow 선택 이유

- main은 항상 깨지지 않는 기준 브랜치로 둡니다.
- 모든 작업은 `feature/<name>-<topic>` 브랜치에서 진행합니다.
- PR과 리뷰를 거쳐 병합하면 작업 이유와 검증 기록이 남습니다.

## Starter 개선 기록

- Sangheon Lee PR 2: `normalize_member_name`이 내부의 여러 공백을 하나로 정리하도록 수정했습니다.
- Sangheon Lee PR 3: `member_initials`가 정리된 이름에서 이니셜을 반환하도록 추가했습니다.
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
member_initials: SL
count_words: 3
is_even: True
```

## 추가 확인 예시

```text
normalize_member_name("  sangheon   lee ") == "Sangheon Lee"
member_name_slug("  sangheon   lee ") == "sangheon-lee"
member_initials("  sangheon   lee ") == "SL"
count_words("Git  flow utility") == 3
count_words("   ") == 0
is_even(4) == True
is_even(5) == False
```
