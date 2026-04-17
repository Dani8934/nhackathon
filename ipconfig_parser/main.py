from pathlib import Path
import json


def is_ip(line):
    return line and ("." in line or ":" in line) and " " not in line


def ipconfig_parser(lines):
    adapters = []
    current = None
    dns_mode = False
    gw_mode = False

    for line in lines:
        line = line.strip()

        # NEW ADAPTER
        if line.endswith(":") and "adapter" in line.lower():
            if current:
                adapters.append(current)

            current = {
                "adapter_name": line[:-1],
                "description": "",
                "physical_address": "",
                "dhcp_enabled": "",
                "ipv4_address": "",
                "subnet_mask": "",
                "default_gateway": [],
                "dns_servers": []
            }

            dns_mode = False
            gw_mode = False
            continue

        if not current:
            continue

        if ":" in line:
            key, value = line.split(":", 1)
            value = value.strip()
        else:
            key = line
            value = ""

        if "Description" in key:
            current["description"] = value
        elif "Physical Address" in key:
            current["physical_address"] = value
        elif "DHCP Enabled" in key:
            current["dhcp_enabled"] = value
        elif "IPv4 Address" in key:
            current["ipv4_address"] = value.split("(")[0].strip()
        elif "Subnet Mask" in key:
            current["subnet_mask"] = value

        elif "DNS Servers" in key:
            dns_mode = True
            gw_mode = False
            if value and is_ip(value):
                current["dns_servers"].append(value)
        elif dns_mode:
            if is_ip(line):
                current["dns_servers"].append(line)
            else:
                dns_mode = False

        elif "Default Gateway" in key:
            gw_mode = True
            dns_mode = False
            if value and is_ip(value):
                current["default_gateway"].append(value)
        elif gw_mode:
            if is_ip(line):
                current["default_gateway"].append(line)
            else:
                gw_mode = False
    
    #utolsó adapter
    if current:
        adapters.append(current)

    return adapters


def main():
    result = []

    for path in sorted(Path(".").glob("*.txt")):
        lines = path.read_text(encoding="UTF-16-LE").splitlines()

        result.append({
            "file_name": path.name,
            "adapters": ipconfig_parser(lines)
        })

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()