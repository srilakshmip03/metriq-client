from metriq import MetriqClient

client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
result = client.submission_get("60f5ce7bc3519e62a97feb54")
assert result is not None
