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
- 이후 `feature/sangheon-amend-log` 브랜치로 push하여 PR에서 변경 의도를 쉽게 확인할 수 있게 했습니다.
- 주의할 점: `git commit --amend`는 마지막 커밋을 새 커밋으로 다시 만드는 작업이므로, 이미 원격에 공유한 커밋에는 함부로 사용하지 않습니다. 공유 후에는 팀원과 먼저 합의하거나, 가능하면 새 커밋으로 수정 이력을 남깁니다.

### 왜 이 방법을 선택했는가(Why)
- 파일 내용에는 문제가 없고, 마지막 커밋 메시지만 모호한 상황이었습니다.
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
- `--soft` 옵션은 작업 내용을 삭제하지 않고 staging area에 남겨두므로, 변경사항을 버리는 reset보다 안전하게 커밋만 다시 만들 수 있습니다.
- push 전 로컬 커밋 정리 상황이라 협업 중인 원격 히스토리에 영향을 주지 않았습니다.

## 시나리오: revert
### 참여자
- giyeop-cody

### 상황
- `docs/troubleshooting-log.md`에 실수로 `temporary wrong note`라는 임시 메모를 추가한 커밋을 만들었습니다.
- 해당 커밋은 이미 하나의 커밋으로 기록된 상태였기 때문에, 단순히 파일만 되돌리는 것보다 "이 커밋을 취소했다"는 이력을 남기는 방식이 필요했습니다.
- 협업 상황에서는 이미 공유될 수 있는 커밋을 `reset`으로 없애면 다른 팀원의 히스토리와 충돌할 수 있으므로, 새 취소 커밋을 만드는 `git revert` 흐름을 실습했습니다.

### 시도한 명령/절차
- `printf '\ntemporary wrong note\n' >> docs/troubleshooting-log.md`
- `git add docs/troubleshooting-log.md`
- `git commit -m "docs: add temporary wrong note"`
- `git revert --no-edit HEAD`

### 결과
- `docs: add temporary wrong note` 커밋으로 추가했던 임시 메모가 제거되었습니다.
- `git revert --no-edit HEAD`는 기존 커밋을 삭제하지 않고, 해당 커밋의 변경사항을 반대로 적용하는 새 커밋을 만들었습니다.
- 따라서 `git log`에는 실수한 커밋과 이를 되돌린 커밋이 모두 남아, 어떤 변경을 왜 취소했는지 추적할 수 있습니다.
- 주의할 점: revert는 히스토리를 보존하는 방식이라 공유 브랜치에서 reset보다 안전하지만, 되돌리는 대상 커밋 이후에 같은 파일을 수정한 변경이 있으면 충돌이 발생할 수 있습니다. 충돌이 나면 파일을 정리한 뒤 revert를 계속 진행해야 합니다.

### 왜 이 방법을 선택했는가(Why)
- `reset`은 커밋 이력을 되감아 로컬 히스토리 자체를 바꾸는 명령이므로, 이미 원격에 push했거나 팀원이 기반으로 삼았을 수 있는 커밋에는 위험합니다.
- `revert`는 취소 이력을 새 커밋으로 남기기 때문에 협업 중인 브랜치에서도 변경의 흐름을 안전하게 공유할 수 있습니다.
- 이번 상황은 "잘못된 변경을 없애되, 그 변경을 취소했다는 기록은 남겨야 하는 경우"였으므로 `git revert`가 적절했습니다.

## 시나리오: stash
### 참여자
- giyeop-cody

### 상황
- `docs/troubleshooting-log.md`를 수정하던 중 아직 커밋하기 애매한 `stash scratch line` 임시 변경이 작업 트리에 남아 있었습니다.
- 다른 작업을 확인하거나 브랜치를 전환하기 전에는 작업 트리가 깨끗해야 하는 경우가 많습니다.
- 아직 커밋으로 남길 수준은 아니지만 수정 내용을 버리고 싶지도 않았기 때문에, 임시 보관 후 다시 복원하는 `stash` 흐름을 실습했습니다.

### 시도한 명령/절차
- `printf '\n- stash scratch line\n' >> docs/troubleshooting-log.md`
- `git stash`
- `git status`
- `git stash pop`

### 결과
- `git stash` 실행 후 작업 트리의 임시 변경이 stash 목록으로 이동했고, `git status`에서 커밋할 변경사항이 없는 깨끗한 상태를 확인할 수 있었습니다.
- `git stash pop`을 실행하자 보관해 둔 `stash scratch line` 변경이 다시 작업 트리에 적용되었습니다.
- stash는 커밋을 만들지 않고 로컬에만 임시 저장하므로 원격 히스토리에는 영향을 주지 않습니다.
- 주의할 점: `git stash pop`은 stash를 적용한 뒤 목록에서 제거합니다. 적용 중 충돌이 발생할 수 있으므로, 중요한 임시 작업은 `git stash list`로 확인하거나 필요하면 `git stash apply`처럼 stash를 남기는 방식도 고려합니다.

### 왜 이 방법을 선택했는가(Why)
- 임시 변경은 아직 팀 이력에 남길 정도로 완성되지 않았지만, 곧 다시 사용할 수 있어 버리면 안 되는 내용이었습니다.
- `stash`를 사용하면 커밋을 만들지 않고도 작업 트리를 빠르게 비울 수 있어 브랜치 전환, pull, 다른 실습 확인을 안전하게 진행할 수 있습니다.
- `stash pop`으로 보관한 변경을 다시 가져올 수 있으므로, 짧은 중단이 필요한 작업 흐름에 적합했습니다.
