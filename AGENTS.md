# Daily Algorithm Repository Guidelines

## Project Structure

- Each problem under `Daily_Algoithm` is a separate C# console project.
- Use the dated problem folder name (e.g. `2026-10-16_교대하는 신호`) as the project display name in the shared solution.
- The shared solution is `Daily_Algoithm/Daily_Algoithm.sln`.
- A per-problem `.sln` file is optional. The shared solution is the primary entry point for Rider.

## Code Preservation

- Never overwrite, delete, or replace existing problem statements or user-written code.
- New `.cs` files must be completely empty until the user writes code.
- Do not add `Main`, top-level statements, templates, or placeholder comments to new `.cs` files.
- Do not require a successful build while a new `.cs` file is empty.

## 블로그 글 작성 지침

내가 “블로그에 정리할 수 있게 글을 적어줘”라고 하면, 내가 제공한 코드를 바탕으로 블로그에 바로 붙여 넣을 수 있는 마크다운 글을 작성해줘.

## 작성 방식

- 글 전체를 하나의 `markdown` 코드 블록에 담아줘.
- `~한다`, `~이다` 문체를 사용하고, 처음 코드를 읽는 사람도 실행 흐름을 따라갈 수 있게 설명해줘.
- 내가 작성한 코드를 기준으로 설명해줘. 변수명, 조건식, 자료구조, 반복문 구조는 코드에 적힌 그대로 사용해줘.
- 내가 제공한 문장이나 형식을 그대로 유지해 달라고 하면 제목 단계, 표 구조, 문장 표현을 임의로 바꾸지 마.
- 내가 요청한 범위의 본문만 작성해줘. 문제 전문, 전체 코드, 복잡도 분석은 따로 요청했을 때 추가해줘.

## 글의 구성

### 코드 실행 과정

프로그래머스 문제 풀이를 정리할 때는 해당 문제의 **공식 입출력 예**를 사용해줘. 내가 문제 설명과 입출력 예를 제공했다면 그 내용을 기준으로 하고, 공식 예제가 여러 개라면 내가 지정한 예제를 우선 사용해줘. 따로 지정하지 않았다면 코드의 핵심 동작을 가장 잘 보여주는 공식 예제 하나를 골라줘.

선택한 예제의 입력값과 기대 반환값을 먼저 제시해줘. 예제 입력은 축약하거나 바꾸지 말고, 전체 입력을 사용해 최종 반환값까지 따라가 줘. 예를 들어 공식 입력이 `[7, 4, 5, 6]`이면 `[7, 4]`로 줄이지 말고 네 트럭 모두의 처리 과정을 보여줘.

실행 과정을 이해하는 데 필요한 규칙도 먼저 짚어줘. 예를 들어 큐의 어느 쪽이 맨 앞인지, `0`이 무엇을 의미하는지 설명해줘.

공식 예제가 대화에 없다면 프로그래머스 문제 페이지에서 확인해줘. 확인할 수 없다면 문제 링크나 입출력 예를 요청해줘.

### 시작 상태

매개변수, 주요 변수, 자료구조의 초기 상태를 `변수 | 값` 표로 정리해줘.

### 1. 첫 번째 실행 단계

이후 제목에도 `### 2. ...`, `### 3. ...`처럼 번호를 붙여줘. 각 제목에는 코드에 해당하는 인덱스와 현재 처리 중인 대상을 포함해줘. 예를 들어 `### 1. i = 0일 때, 7짜리 트럭이 들어간다`처럼 써줘.

각 단계는 다음 방식으로 설명해줘.

1. 표 앞에서 현재 인덱스, 처리 중인 값, 반복을 시작할 때의 상태를 짧게 설명해줘.
2. 표에는 `실행 순서 | 코드가 하는 일 | 자료구조 상태 | 주요 변수 값`을 넣어줘. 자료구조와 변수의 열 이름은 실제 코드에 맞춰 `큐`, `Count`, `onBrideWeight`, `time`처럼 구체적으로 써줘.
3. **표의 값은 각 행의 동작이 끝난 직후**를 기준으로 기록해줘. 조건 검사, 자료구조에 값을 넣거나 빼는 동작, 변수 갱신을 각각 다른 행으로 나눠줘. 값이 바뀌지 않은 열도 그대로 적어줘.
4. 조건식에는 실제 값을 대입하고 참인지 거짓인지 설명해줘. 예를 들어 `Count == bridge_length`는 `2 == 2`이므로 참이라고 써줘.
5. 표 뒤에는 `break`, `continue`, `i++` 등으로 실행 흐름이 어디로 이어지는지 설명해줘. 중첩 반복문이라면 어느 반복문을 빠져나가는지, 다음 반복에서도 같은 인덱스를 검사하는지까지 짚어줘.

### 마지막 단계

반복문이 왜 끝나는지, 종료 직후의 변수 값이 무엇을 의미하는지, 반환 직전에 어떤 계산이 이루어지는지 설명해줘. 마지막에는 예제의 실제 값을 대입해 최종 반환값을 보여주고, 공식 예제의 기대 반환값과 일치하는지 확인해줘.
