# History Cleanup Log

## 작업 개요
Sangheon Lee가 개인 feature 브랜치에서 `git rebase -i`를 사용해 커밋 히스토리를 정리했습니다.

이번 기록은 두 가지 interactive rebase 흐름을 증빙합니다.

- `squash`: 여러 커밋을 하나의 의미 있는 커밋으로 합치는 흐름 확인
- `reword`: 커밋 메시지를 더 명확한 표현으로 수정

공유 브랜치인 `main`에 이미 merge된 커밋은 다시 쓰지 않고, 개인 feature 브랜치의 커밋만 정리했습니다.

## 작업 브랜치
- 브랜치: `feature/sangheon-history-cleanup`
- 기준 브랜치: `main`
- 주요 대상 파일: `docs/conflict-resolution.md`, `screenshot/*`

## Rebase 전 히스토리
`git rebase -i`를 실행하기 전에는 rename/edit conflict 기록 커밋의 메시지가 다소 짧고, 변경 목적이 충분히 드러나지 않았습니다.

```text
908ec75 docs: document team notes rename edit conflict
2aef5be docs: add team notes review checklist
7e71ad3 Merge pull request #19 from codyssey-b2-2-team-mission/feature/giyeop-rename-team-notes
```

## Interactive Rebase 진행
### squash 흐름 확인
먼저 `squash`를 사용해 두 커밋을 하나로 합치는 흐름을 확인했습니다.

![interactive rebase squash todo](<../screenshot/Screenshot 2026-05-20 at 8.38.28 PM.png>)

커밋 메시지 편집 화면에서는 두 커밋 메시지가 함께 표시되어, 어떤 메시지를 최종 커밋에 남길지 정리할 수 있음을 확인했습니다.

![squash commit message editor](<../screenshot/Screenshot 2026-05-20 at 8.38.48 PM.png>)

### reword 적용
최종 정리에서는 `reword`를 사용해 rename/edit conflict 문서화 커밋 메시지를 더 구체적으로 바꾸었습니다.

```text
pick 2aef5be docs: add team notes review checklist
reword 908ec75 docs: document team notes rename edit conflict
```

![interactive rebase reword todo](<../screenshot/Screenshot 2026-05-20 at 9.02.33 PM.png>)

커밋 메시지는 다음처럼 수정했습니다.

```text
docs: record team notes rename edit conflict resolution
```

![reword commit message editor](<../screenshot/Screenshot 2026-05-20 at 9.03.01 PM.png>)

## Rebase 후 히스토리
rebase 이후 커밋 메시지가 변경 목적과 결과를 더 명확하게 설명하도록 정리되었습니다.

```text
34d7511 docs: record team notes rename edit conflict resolution
d8c8220 docs: add team notes review checklist
7e71ad3 Merge pull request #19 from codyssey-b2-2-team-mission/feature/giyeop-rename-team-notes
```

## 비교 결과
- rebase 전에는 `docs: document team notes rename edit conflict` 메시지가 기록 대상만 설명했습니다.
- rebase 후에는 `docs: record team notes rename edit conflict resolution`으로 변경되어, rename/edit conflict의 해결 기록을 남겼다는 목적이 더 분명해졌습니다.
- `squash` 화면을 통해 여러 커밋을 하나로 합치는 방법을 확인했고, 실제 최종 정리에는 변경 목적을 보존하기 위해 `reword`를 사용했습니다.
- 정리 대상은 개인 feature 브랜치의 커밋으로 제한하여 공유된 `main` 히스토리를 다시 쓰지 않았습니다.

## Validation
```sh
git rebase -i HEAD~2
git log --oneline --decorate -3
git status
```
