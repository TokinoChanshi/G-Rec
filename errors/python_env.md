# Python Environment & Dependency Troubleshooting

## Common Issues in This Project

### 1. `tyro` or `docstring_parser` not found
- **Cause**: These are dependencies of LivePortrait that sometimes get missed or version-conflicted.
- **Solution**:
    ```bash
    pip install tyro docstring_parser
    ```

### 2. `DeepFilterNet` Installation Failure
- **Symptom**: `pip install deepfilternet` fails with Rust/Cargo errors or network timeouts.
- **Solution**:
    - Ensure Microsoft C++ Build Tools are installed.
    - Try installing the pre-built wheel if available.
    - Check internet connection (GFW issues in CN).

### 3. `cv2` (OpenCV) Loading Error
- **Symptom**: `cv2.error: (-215:Assertion failed) !buf.empty()`
- **Cause**: Windows paths containing Chinese characters (e.g., `博客视频`) cause standard `cv2.imread` to fail.
- **Fix (Pattern)**:
    Replace:
    ```python
    img = cv2.imread(path)
    ```
    With:
    ```python
    import numpy as np
    img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)
    ```
