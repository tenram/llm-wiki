# linux-dash

> Source: https://github.com/tariqbuilds/linux-dash
> Collected: 2026-08-24
> Published: Unknown (v2.0)

A simple & low-overhead web dashboard for Linux systems. Under 400KB on disk, minimalist UI, drop-in installation. Four server stacks included: Node.js (recommended), Go, Python, PHP.

## Installation

```sh
git clone --depth 1 https://github.com/afaqurk/linux-dash.git
cd linux-dash/app/server
```

Node.js (recommended):
```sh
npm install --production
node index.js   # port 80 default; LINUX_DASH_SERVER_PORT / --port to override
                # listens on 0.0.0.0; LINUX_DASH_SERVER_HOST / --host to override
```

Go: `go run index.go` (or build a binary). Python: `python index.py`.

PHP: enable exec/shell_exec/escapeshellarg, point web server (Apache/nginx) at the app/ directory.

## Security

> "It is strongly recommended that all linux-dash installations be protected via a security measure of your choice."
> "Linux Dash does not provide any security or authentication features."

No built-in auth; firewall or reverse-proxy protection is mandatory.

## Operational notes (2026 observation)

Effectively unmaintained: last push 2024-04, issue creation restricted, open injection-vulnerability issue (#498) never fixed. Metrics engine is a bash script (`linux_json_api.sh`) shelling to coreutils/procfs: CPU, RAM/swap, disk usage + I/O, per-interface bandwidth, processes, Docker containers, users/logins, cron, network connections, ARP. Extra binaries needed for full coverage: net-tools (netstat/ifconfig/arp), lm-sensors (temps), bind9-dns-utils (dig). Known issues: PHP-mode JSON escaping bugs (#427), Node JSON serialization errors (#508/#521), egrep deprecation warnings.
