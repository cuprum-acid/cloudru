# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.18+
- Ubuntu 22.04 LTS

## Usage

```yaml
- name: Install and configure Docker
  hosts: all
  roles:
    - role: docker
      become: true
```
