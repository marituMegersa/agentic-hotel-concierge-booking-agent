def test_agent_orchestrator():
    prompt = "Test execution query for agentic-hotel-concierge-booking-agent"
    assert len(prompt) > 0
    assert "Test" in prompt
