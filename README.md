# korullm

`korullm` is the LLM boundary extracted from Koru. It provides strategy
selection, policy-resolved SubLLM transports and a fail-closed Cursor SDK lane.

Koru owns task orchestration, browser/IDE control and business policies. This
package owns only model selection and model invocation.

## Installation

```bash
pip install korullm
pip install 'korullm[cursor]'
```

## Usage

```python
from pathlib import Path
from korullm import run_subllm

result = run_subllm(
    "Return a JSON plan.",
    Path.cwd(),
    route_function="planning-assistant",
    system_prompt="Return only valid JSON.",
)
assert result.returncode == 0
```

The model and credentials are resolved by SubLLM for the `koru-agent` route;
callers do not select providers or read secret values directly.
