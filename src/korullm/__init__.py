"""Koru LLM backend strategies.

Each LLM provider (IDE chat, Codex, Claude, GPT, Ollama) owns its own
retry/idle/prompt-envelope policy. The autonomous loop must not branch
on env var names inline — it asks the registry.
"""

from korullm.strategies import (  # noqa: F401 — register concrete strategies
    claude,
    codex,
    gpt,
    ide_chat,
    ollama,
)
from korullm.strategies.base import (
    DriveFailureAssessment,
    LlmCapabilities,
    LlmStrategy,
)
from korullm.strategies.ide_chat import IdeChatStrategy
from korullm.strategies.registry import (
    get_llm_strategy,
    list_llm_strategy_ids,
    register_llm_strategy,
    resolve_active_llm_strategy,
    resolve_llm_strategy_from_environment,
)
from korullm.cursor import CursorLlmResult, run_cursor_llm
from korullm.subllm import SubLlmResult, probe_subllm_route, run_subllm, run_subllm_messages

__all__ = [
    "DriveFailureAssessment",
    "LlmCapabilities",
    "LlmStrategy",
    "IdeChatStrategy",
    "get_llm_strategy",
    "list_llm_strategy_ids",
    "register_llm_strategy",
    "resolve_active_llm_strategy",
    "resolve_llm_strategy_from_environment",
    "CursorLlmResult",
    "SubLlmResult",
    "run_cursor_llm",
    "probe_subllm_route",
    "run_subllm",
    "run_subllm_messages",
]
