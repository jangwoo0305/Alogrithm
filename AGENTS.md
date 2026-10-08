# Daily algorithm projects

When creating or preparing a problem under `Daily_Algoithm`, register its `.csproj` in `Daily_Algoithm/Daily_Algoithm.sln` as part of the same task. Do not leave registration as a manual step for the user.

- Keep each problem as a separate console project so its entry point does not conflict with other problems.
- Use the dated problem folder name as the solution project display name.
- Prefer `dotnet sln Daily_Algoithm/Daily_Algoithm.sln add <project-path> --in-root` when a .NET SDK is available. Otherwise safely edit the existing solution's Project/EndProject entry and ProjectConfigurationPlatforms mappings for every existing solution configuration.
- Preserve existing projects, configurations, problem statements, and user code. Never duplicate an already registered project.
- Verify the solution references the new project through a valid relative path and contains its configuration mappings before reporting completion.
- Tell the user to open the shared `Daily_Algoithm.sln` in Rider. A per-problem solution, if created, is optional and does not replace shared-solution registration.
- New C# files must remain completely empty until the user writes code. Do not add an entry point or require a successful build while the file is empty.
