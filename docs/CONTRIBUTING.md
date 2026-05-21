# Contributing Guide

## 브랜치 전략(GitHub Flow)

- `main`: 항상 배포 가능하고, 팀 기준에서 깨지지 않는 상태를 유지합니다.
- `feature/*`: 이슈 단위 작업 브랜치이며, `main`에서 분기하고 PR로만 병합합니다.
- 병합 전에는 최신 `main`을 반영하고, 충돌이나 테스트 결과를 PR에 기록합니다.

우리 팀이 GitHub Flow를 선택한 이유:
- 브랜치 전략이 단순해서 3인 팀 실습에서 작업 흐름을 빠르게 맞출 수 있습니다.
- 모든 변경이 PR과 리뷰를 거치므로 협업 증빙을 남기기 쉽습니다.
- 충돌 해결, 리뷰 반영, 트러블슈팅 기록을 작은 단위로 추적할 수 있습니다.

## 브랜치 네이밍 규칙

- 형식: `feature/<name>-<topic>`
- 예시: `feature/sangheon-name-normalizer`

## 커밋 메시지 컨벤션

- `feat: add word count utility`
- `fix: handle member name spacing`
- `docs: record reset soft scenario`
- `test: add utility assertions`

금지 예: `update`, `fix`, `temp`, `wip`, `final`, `bug fix`, `edit file`

## PR 규칙

- PR 본문에는 `What`, `Why`, `How(테스트/검증 방법)`를 반드시 작성합니다.
- 모든 작업은 Issue를 생성한 뒤 진행하고, PR 본문에는 `Closes #<issue_number>` 또는 `Fixes #<issue_number>`를 포함합니다.
- 모든 `feature/*` 브랜치는 PR로만 `main`에 병합합니다.
- 병합 조건은 최소 1명 승인, 실질적인 리뷰 코멘트 1개 이상, 모든 리뷰 대화 해결, 충돌 없음입니다.
- 작성자는 리뷰 코멘트마다 답글 또는 수정 커밋으로 응답합니다.

## 코드 리뷰 규칙

- `LGTM`만 남기는 리뷰는 금지합니다.
- 리뷰 코멘트는 파일/라인 근거와 질문, 위험, 대안, 개선 이유 중 하나 이상을 함께 작성합니다.

## 충돌 대응 흐름

- 충돌 발생 → 충돌이 난 브랜치 작성자가 팀에 공유 → 해결 전략 선택 → 검증 → 커밋 → `docs/conflict-resolution.md`에 상황/절차/결과/주의점을 기록

## 안전 규칙

- `main`에 force push하지 않습니다.
- 팀 합의 없이 공유 브랜치에서 rebase하지 않습니다.
- 공유 히스토리는 팀 합의 없이 다시 쓰지 않습니다.
- 이미 공유된 커밋은 가능하면 `git revert`로 취소합니다.
