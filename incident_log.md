# Sample Incident Log

## INC-001 – System Downtime
- Severity: P1
- Symptoms: Users cannot access the platform.
- Evidence: Health checks fail; application service is unavailable.
- Action: Validate infrastructure and deployment status; follow approved recovery/rollback process.
- Workaround: Approved alternate communication channel.
- Verification: Login, messaging and file access tested successfully.
- Prevention: Availability monitoring and tested rollback.

## INC-002 – Slow Performance
- Severity: P2
- Symptoms: Pages/messages take 8–15 seconds.
- Evidence: Elevated API latency and database resource usage.
- Action: Investigate slow query/configuration change; optimize or rollback approved change.
- Workaround: Communicate degraded performance and prioritize urgent work.
- Verification: Response time returns to baseline.
- Prevention: Performance alerts and pre-release performance testing.

## INC-003 – Login Failure
- Severity: P2
- Symptoms: Valid users cannot sign in.
- Evidence: Authentication logs show failed requests.
- Action: Check identity provider, account status, session/MFA configuration.
- Workaround: Approved account recovery.
- Verification: Test account successfully signs in.
- Prevention: Identity monitoring and clearer recovery process.

## INC-004 – Message Delivery Failure
- Severity: P2
- Symptoms: Messages remain pending.
- Evidence: Queue/delivery logs show processing errors.
- Action: Check queue, backend and database; safely retry.
- Workaround: Alternate approved communication.
- Verification: End-to-end test message delivered.
- Prevention: Queue depth alerts and retry/dead-letter handling.
