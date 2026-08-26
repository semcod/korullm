from __future__ import annotations

import os
from unittest import mock

from korullm import IdeChatStrategy, list_llm_strategy_ids, resolve_active_llm_strategy


def test_shipped_strategies_are_registered() -> None:
    assert {"ide_chat", "openai", "anthropic", "ollama", "codex"}.issubset(
        list_llm_strategy_ids()
    )


def test_default_strategy_is_ide_chat() -> None:
    with mock.patch.dict(os.environ, {}, clear=True):
        assert resolve_active_llm_strategy().id == "ide_chat"


def test_input_busy_uses_cooldown() -> None:
    assessment = IdeChatStrategy().assess_drive_failure(
        {"verification": "input_busy"}, attempt=0, max_attempts=3
    )
    assert assessment.kind == "skip_cooldown"
