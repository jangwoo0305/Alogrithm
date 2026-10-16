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