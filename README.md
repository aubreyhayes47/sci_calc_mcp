# 📘 **sci_calc_mcp**
### A Scientific Calculator MCP Server  
Built with **FastMCP**, designed for **ChatGPT Apps**, **MCP Inspector**, and **Render** deployment.

---

## 🚀 Overview

`sci_calc_mcp` is a lightweight, high-performance **Model Context Protocol (MCP)** server that exposes scientific calculator operations as **atomic tools**.

Each operation is a standalone MCP tool:

- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b)`
- `mod(a, b)`
- `power(base, exponent)`
- `sqrt(x)`
- `sin(x)`
- `cos(x)`
- `tan(x)`
- `asin(x)`
- `acos(x)`
- `atan(x)`
- `exp(x)`
- `ln(x)`
- `log10(x)`
- `absval(x)`
- `round_to(x, digits)`

This design is **MCP-native**, strongly typed, easy to inspect, and ideal for building calculator UIs.

---

## ✨ Features

- 🧮 **Multiple scientific-level operations**
- ⚡ **Pure FastMCP server — minimal dependencies**
- 🌐 **HTTP/SSE transport for web apps and inspectors**
- 📦 **Single-file server (`main.py`)**
- 🔍 Compatible with **MCP Inspector**
- 🤖 Fully compatible with **ChatGPT Apps SDK**
- ☁️ Pre-configured for **Render.com** hosting
- 🔒 Safe mathematical operations (e.g., division by zero protection)

