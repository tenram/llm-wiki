# Frappe HR

> Sources: Frappe Technologies, Unknown date
> Raw: [Frappe HR README](../../raw/hr-management/2026-10-13-frappe-hrms.md)

## Overview

Frappe HR is an open-source, modern HR and payroll software (HRMS) built by Frappe Technologies, offering over 13 modules covering employee management, onboarding, leaves, payroll, and taxation. It began as a module set within ERPNext; from ERPNext version 14 onward, as the modules matured, Frappe HR was split into a separate product. The stated motivation was the absence of any "true" open-source HR and payroll software.

## Key Modules

- **Employee Lifecycle**: onboarding, promotions and transfers, exit interviews and feedback documentation.
- **Leave and Attendance**: leave policies, regional holiday pulling, geolocation-captured check-in/check-out, leave-balance and attendance reports.
- **Expense Claims and Advances**: employee advances, expense claims, multi-level approval workflows, with integration to ERPNext accounting.
- **Performance Management**: goals aligned to key result areas (KRAs), self-evaluation, and appraisal cycles.
- **Payroll & Taxation**: salary structures, income-tax slabs, standard payroll runs, additional/off-cycle payments, and salary-slip income breakup.
- **Mobile App**: leave application/approval, check-in/check-out, and employee profile access on the go.

## Technical Foundation

Built on the Frappe Framework, a full-stack Python/Javascript web application framework providing a database abstraction layer, user authentication, and a REST API; and Frappe UI, a Vue-based component library for single-page frontends.

## Deployment

Managed hosting is available via Frappe Cloud, an open-source platform handling installation, setup, upgrades, monitoring, and maintenance. Self-hosting options: Docker (`docker-compose up` in `hrms/docker`, site at `localhost:8000`, default credentials `Administrator`/`admin`) or a local Frappe bench install (`bench new-site`, `bench get-app erpnext`, `bench get-app hrms`, `bench --site ... install-app hrms`).
