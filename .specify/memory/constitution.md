<!--
Sync Impact Report:
- Version change: [TEMPLATE] -> 1.0.0
- Modified principles:
  - [PRINCIPLE_1_NAME] -> I. Simulation First
  - [PRINCIPLE_2_NAME] -> II. Readability Over Micro-Optimization
  - [PRINCIPLE_3_NAME] -> III. Comprehensive Documentation
  - Removed PRINCIPLE_4 and PRINCIPLE_5 from template
- Added sections: None
- Removed sections: None
- Templates requiring updates (⚠ pending):
  - .specify/templates/plan-template.md (Needs simulation testing added as a Constitution Check gate)
  - .specify/templates/tasks-template.md (Needs documentation and simulation steps formalized)
- Follow-up TODOs: None
-->
# Robotic Arm with Object Sorting Constitution

## Core Principles

### I. Simulation First
All physical movements, algorithms, and control logic MUST be tested and verified in a simulation or dry-run environment before being deployed to the physical robotic arm.
*Rationale: Prevents physical damage to the hardware components, verifies path planning and kinematics, and ensures baseline functionality without risking the physical equipment.*

### II. Readability Over Micro-Optimization
Code MUST be easily readable and understandable by all team members (Hardware, Software, Integration). Clear, maintainable logic and expressive variable names are prioritized over saving minimal memory or CPU cycles.
*Rationale: As a collaborative college project with cross-functional roles, understandable code facilitates easier debugging, code reviews, and smoother handoffs between team members.*

### III. Comprehensive Documentation
Every function, control interface, and hardware wiring configuration MUST be strictly documented. Changes to pinouts or control signals must be reflected in the documentation immediately.
*Rationale: Ensures that hardware and software engineers stay in sync. Outdated or missing documentation leads to integration failures and wasted debugging time.*

## Constraints & Standards

- Hardware constraints (e.g., motor torque limits, sensor accuracy) must be clearly stated in the documentation.
- Software should follow a uniform styling guide to support the Readability principle.

## Development Workflow & Quality Gates

- **Simulation Gate**: Code cannot be merged or deployed to hardware without a video or log proving successful simulation.
- **Review Gate**: All new code MUST be peer-reviewed for readability and documentation compliance. A feature is only considered "Done" if it passes simulation tests successfully and the corresponding hardware/software documentation is fully updated.

## Governance

This Constitution supersedes all other practices for the Robotic Arm with Object Sorting project. 
Amendments require team discussion, documentation of the change, and a version bump according to Semantic Versioning:
- MAJOR: Backward incompatible governance/principle removals.
- MINOR: New principle/section added.
- PATCH: Clarifications and wording fixes.

All PRs/reviews must verify compliance with these core principles.

**Version**: 1.0.0 | **Ratified**: 2026-05-01 | **Last Amended**: 2026-05-01
