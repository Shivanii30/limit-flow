# Limitflow

A plug-and-play Python rate limiting library with Redis backend, supporting multiple algorithms and advanced adaptive protection mechanisms.

Built to simulate real-world backend traffic control systems used in high-scale APIs.

---

## What it does?

- Control request traffic
- Prevent abuse (spam, bots, brute-force)
- Adapt dynamically to different load patterns

Works seamlessly with:
- FastAPI
- Flask
- Django (extendable)

---

## ⚙️ Features

**Rate Limiting Algorithms**
- Token Bucket
- Sliding Window
- Fixed Window

**Cost-based limiting**
- Different endpoints consume different "cost units"
- Example: `/heavy` > `/light`

**WAF-style escalation**
- Tracks user violations
- Applies progressive actions:
- Warn → Limit → Block

**Redis-backed storage**
- Distributed & scalable
- Suitable for multi-instance systems

---

## Performance Tested

- Load tested using Locust
- Sustained ~200+ requests/sec
- Controlled failure responses (429) under overload
- Demonstrated realistic API protection behavior

---

## Future Improvements

- Adaptive rate limiting (auto-tighten/relax limits)
- Violation logging + JSON export
- Dashboard for monitoring
- PyPI release (`pip install rateshield`)
- Middleware support for more frameworks

---

## 🤝 Contributing

Contributions are welcome!

Feel free to:
- Improve algorithms
- Add new strategies
- Optimize Redis usage
- Add integrations

---


## ⭐ If you like this project

Give it a star and share feedback!
