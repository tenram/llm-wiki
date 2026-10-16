# pfSense

> Sources: Rubicon Communications, LLC (Netgate), Unknown date
> Raw: [pfSense README](../../raw/networking-tools/2026-10-13-pfsense.md)

## Overview

pfSense is a free network firewall distribution based on the FreeBSD operating system, with a custom kernel and third-party free software packages. Its package system aims to match or exceed the functionality of common commercial firewalls without artificial limitations, and it has replaced products from Check Point, Cisco (PIX/ASA), Juniper, SonicWall, Netgear, Watchguard, and Astaro in production deployments.

## Configuration Model

All components are configured through a web interface; no UNIX knowledge, command-line use, or manual rule-set editing is required. Users familiar with commercial firewalls adapt quickly, though commercial-grade firewall newcomers face a learning curve.

## History and Licensing

Started in 2004 as a fork of the m0n0wall project (which ended 2015-02-15), diverging significantly since. Copyright 2004-2026 Rubicon Communications, LLC (Netgate), published under an open-source license. The project is funded partly through bundled hardware appliances and commercial support.

## See Also

- [ZeroTier](zerotier.md) — software-defined networking platform; overlaps in the networking-tools domain but serves SDN/connectivity rather than firewall filtering.
