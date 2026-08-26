from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

from korullm import subllm


def test_subllm_transport_uses_policy_route(monkeypatch) -> None:
    observed: dict[str, object] = {}

    def complete(application, function, messages, **kwargs):
        observed.update(application=application, function=function, messages=messages, **kwargs)
        return SimpleNamespace(
            content='{"ok":true}', provider="zai", model="glm-5.3", usage={"total_tokens": 7}
        )

    monkeypatch.setattr(subllm, "_runtime", lambda: (complete, lambda **_kwargs: {}))
    result = subllm.run_subllm(
        "plan", Path("/workspace"), route_function="planning-assistant", timeout_seconds=12
    )

    assert result.returncode == 0
    assert result.model == "zai/glm-5.3"
    assert observed["application"] == "koru-agent"
    assert observed["function"] == "planning-assistant"
    assert observed["timeout_seconds"] == 12


def test_subllm_transport_fails_closed_when_runtime_missing(monkeypatch) -> None:
    def unavailable():
        raise ImportError("subllm missing")

    monkeypatch.setattr(subllm, "_runtime", unavailable)
    result = subllm.run_subllm("plan", Path("/workspace"), route_function="planning-assistant")
    assert result.returncode == 1
    assert "subactor-subllm" in result.stderr
