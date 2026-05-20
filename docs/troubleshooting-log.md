# Troubleshooting Log

## 시나리오: amend
### 참여자
- Sangheon Lee

### 상황
- `docs/troubleshooting-log.md`의 amend 시나리오를 작성한 뒤 처음에는 커밋 메시지를 `docs: update`로 작성했습니다.
- 이 메시지는 어떤 문서를 왜 수정했는지 드러나지 않아 PR 목록이나 `git log`에서 변경 의도를 파악하기 어려웠습니다.
- 아직 원격 브랜치에 push하기 전이었기 때문에, 새 커밋을 추가로 만들기보다 마지막 커밋 메시지를 바로 고치는 방식으로 정리했습니다.

### 시도한 명령/절차
- `git add docs/troubleshooting-log.md`
- `git commit -m "docs: update"`
- `git commit --amend -m "docs: record amend scenario"`
- `git push -u origin feature/sangheon-amend-log`

### 결과
- 마지막 커밋 메시지가 `docs: update`에서 `docs: record amend scenario`로 변경되었습니다.
- 커밋의 변경 내용은 유지하면서, amend 시나리오를 기록했다는 목적이 더 분명해졌습니다.
- 이후 `feature/sangheon-amend-log` 브랜치로 push하여 PR에서 변경 의도를 쉽게 확인할 수 있게 되었습니다.
- 주의할 점: `git commit --amend`는 마지막 커밋을 새 커밋으로 다시 만드는 작업이므로, 이미 원격에 공유한 커밋에는 함부로 사용하지 않습니다. 공유 후에는 팀원과 먼저 합의하거나, 가능하면 새 커밋으로 수정 이력을 남깁니다.

### 왜 이 방법을 선택했는가(Why)
- 파일 내용에는 문제가 없고 마지막 커밋 메시지만 모호한 상황이었습니다.
- 아직 push 전이라 협업 중인 원격 히스토리에 영향을 주지 않았기 때문에 `git commit --amend`가 가장 단순하고 적절했습니다.
- 불필요한 추가 커밋을 만들지 않고, 하나의 커밋에 정확한 의도와 변경 내용을 함께 담을 수 있었습니다.

## 시나리오: reset
### 참여자
- KANGSIK-SEO

### 상황
- `docs/troubleshooting-log.md`의 reset soft 시나리오를 작성한 뒤 처음에는 커밋 메시지를 `update`로 작성했습니다.
- 이 메시지는 어떤 Git 상황을 기록했는지 알기 어렵고, 팀 커밋 메시지 규칙에서도 금지한 모호한 표현입니다.
- 아직 원격 브랜치에 push하기 전이었기 때문에, 커밋만 취소하고 같은 변경사항은 그대로 유지한 뒤 더 명확한 메시지로 다시 커밋했습니다.

### 시도한 명령/절차
- `git add docs/troubleshooting-log.md`
- `git commit -m "update"`
- `git reset --soft HEAD~1`
- `git commit -m "docs: record reset soft scenario"`
- `git push -u origin feature/kangsik-reset-soft-log`

### 결과
- `update` 커밋은 로컬 히스토리에서 사라졌습니다.
- 문서 변경사항은 사라지지 않고 staged 상태로 유지되어 바로 다시 커밋할 수 있었습니다.
- 최종 커밋 메시지는 `docs: record reset soft scenario`가 되어 변경 목적이 더 명확해졌습니다.
- 주의할 점: `git reset --soft HEAD~1`은 변경사항을 보존하지만 커밋 이력을 되돌립니다. 이미 원격에 push한 공유 커밋에는 팀 합의 없이 reset을 사용하지 않고, 보통 `git revert`를 우선 검토합니다.

### 왜 이 방법을 선택했는가(Why)
- 파일 내용은 유지하고 커밋 메시지만 더 좋은 형태로 다시 만들고 싶었습니다.
- `--soft` 옵션은 작업 내용을 삭제하지 않고 staging area에 남겨두므로, destructive reset보다 안전하게 커밋만 다시 만들 수 있습니다.
- push 전 로컬 커밋 정리 상황이라 협업 중인 원격 히스토리에 영향을 주지 않았습니다.

## 시나리오: revert
### 참여자
- giyeop-cody

### 상황
- 문제가 무엇이었는지(재현 가능한 설명)

### 시도한 명령/절차
- (예) `git revert`

### 결과
- 무엇이 어떻게 해결됐는지
- 주의할 점(특히 원격 히스토리/협업 영향)

### 왜 이 방법을 선택했는가(Why)
- reset 대신 revert를 선택한 이유 등

## 시나리오: stash
### 참여자
- giyeop-cody

### 상황
- 문제가 무엇이었는지(재현 가능한 설명)

### 시도한 명령/절차
- (예) `git stash`
- (예) `git stash pop`

### 결과
- 무엇이 어떻게 해결됐는지
- 주의할 점(특히 원격 히스토리/협업 영향)

### 왜 이 방법을 선택했는가(Why)
- stash를 선택한 이유
temporary wrong note
