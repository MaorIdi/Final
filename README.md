# Virtual Machine Infrastructure Simulator

A Python-based virtual machine infrastructure simulator that allows users to create, configure, and manage virtual machines through an interactive command-line interface.

## Features

- **Interactive VM Creation**: Create virtual machines by specifying CPU, memory, and disk requirements
- **Data Validation**: Input validation using Pydantic models to ensure data integrity
- **Configuration Persistence**: Save VM configurations to JSON files for later use
- **Automated Provisioning**: Simulate VM setup and software installation (Nginx simulation included)
- **Configurable Logging**: Flexible logging system with environment variable control for console/file-only modes
- **Batch Processing**: Configure multiple VMs from saved configuration files

## Project Structure

```
Final/
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── run.sh                     # Convenience script to run the application
├── configs/
│   └── instances.json         # VM configurations storage
├── logs/
│   └── provisioning.log       # Application logs
├── scripts/
│   └── init_vm.sh            # VM initialization script (Nginx installation simulation)
└── src/
    ├── infra_simulator.py     # Main application logic
    ├── machine.py            # VM data model (Pydantic)
    └── __pycache__/          # Python cache files
```

## Requirements

- Python 3.7+
- Bash (for running initialization scripts)
- Dependencies listed in `requirements.txt`

## Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd Final
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure script permissions** (Linux/macOS)
   ```bash
   chmod +x scripts/init_vm.sh
   ```

## Usage

### Running the Simulator

You have several options to run the simulator:

**Option 1: Using the convenience script**
```bash
./run.sh
```

**Option 2: Direct execution**
```bash
cd src
python infra_simulator.py
```

**Option 3: With custom logging mode**
```bash
# Run with logs-only mode (no console output)
LOGGING_MODE=logs_only python src/infra_simulator.py

# Run with default mode (console + logs)
LOGGING_MODE=console python src/infra_simulator.py
```

### Interactive VM Creation

The application will prompt you to:

1. **Create a new VM**: Enter 'y' to start creating a virtual machine
2. **Specify VM details**:
   - **Nickname**: A unique identifier for your VM
   - **CPUs**: Number of CPU cores (numeric value)
   - **Memory**: Amount of RAM in MB (numeric value)
   - **Disk**: Storage size in GB (numeric value)

3. **Continue or finish**: Choose whether to create additional VMs

### Example Session

```
Would you like to create a new virtual machine (y/n): y
Enter the nickname of the VM: web-server-01
Enter the number of CPUs: 2
Enter the amount of memory (in MB): 4096
Enter the size of the disk (in GB): 50

Virtual Machine created: name='web-server-01' cpu=2.0 memory=4096.0 disk=50.0

Would you like to create another virtual machine? (y/n): n
```

## Configuration Files

### VM Instances (`configs/instances.json`)

The application automatically saves VM configurations in JSON format:

```json
{
  "vms": [
    {
      "name": "web-server-01",
      "cpu": 2.0,
      "memory": 4096.0,
      "disk": 50.0
    }
  ]
}
```

### Requirements (`requirements.txt`)

Current dependencies:
- `pydantic==2.11.7`: Data validation and parsing using Pydantic v2
- `pydantic_core==2.33.2`: Core functionality for Pydantic
- `annotated-types==0.7.0`: Type annotations support
- `typing_extensions==4.14.1`: Extended typing support
- `typing-inspection==0.4.1`: Runtime type inspection utilities

## Logging

The application provides flexible logging with environment variable control:

### Logging Modes

- **Default Mode** (console + file): Outputs to both console and `logs/provisioning.log`
- **Logs-only Mode**: Outputs only to the log file, no console output

### Environment Variable Control

Set the `LOGGING_MODE` environment variable to control logging behavior:

```bash
# Default: Both console and file logging
LOGGING_MODE=console python src/infra_simulator.py

# Logs-only: File logging only (no console output)
LOGGING_MODE=logs_only python src/infra_simulator.py

# You can also export the variable for persistent use
export LOGGING_MODE=logs_only
python src/infra_simulator.py
```

### Log Format

```
2025-01-27 10:30:45 - INFO - root - Virtual Machine created: name='web-server-01' cpu=2.0 memory=4096.0 disk=50.0
```

### Log Levels
- **INFO**: General information and successful operations
- **WARNING**: Non-critical issues and validation errors
- **ERROR**: Critical errors and failures

## VM Provisioning

After creating VMs, the system automatically runs provisioning scripts:

- **Script Location**: `scripts/init_vm.sh`
- **Current Function**: Simulates Nginx installation
- **Customizable**: Modify the script to add your own provisioning logic

## Data Model

Virtual machines are represented using Pydantic models with the following schema:

```python
class VirtualMachine(BaseModel):
    name: str      # VM identifier
    cpu: float     # Number of CPU cores
    memory: float  # Memory in MB
    disk: float    # Disk size in GB
```

## Error Handling

The application includes robust error handling:

- **Validation Errors**: Invalid input data is caught and reported
- **File Operations**: Safe file handling with error recovery
- **Script Execution**: Graceful handling of provisioning script failures

## Development

### Adding New Features

1. **Extend the VM Model**: Modify `machine.py` to add new VM properties
2. **Update Input Collection**: Enhance `ask_user_for_vms()` in `infra_simulator.py`
3. **Modify Provisioning**: Update `scripts/init_vm.sh` for new setup requirements

### Running in Development Mode

The application supports different logging modes for development:

```bash
# For debugging: Default console + file logging
python src/infra_simulator.py

# For production/automated runs: File-only logging
LOGGING_MODE=logs_only python src/infra_simulator.py

# Using the convenience script
./run.sh
```

You can also modify the logging configuration directly in `infra_simulator.py` for additional debug information.

## Troubleshooting

### Common Issues

1. **Permission Denied (scripts)**
   ```bash
   chmod +x scripts/init_vm.sh
   chmod +x run.sh
   ```

2. **Module Not Found**
   ```bash
   pip install -r requirements.txt
   ```

3. **Invalid Input Values**
   - Ensure CPU, memory, and disk values are numeric
   - Check that VM names are unique and non-empty

4. **Logging Issues**
   - Check `LOGGING_MODE` environment variable setting
   - Verify `logs/` directory permissions
   - Use `LOGGING_MODE=console` for debugging

### Log Analysis

Check `logs/provisioning.log` for detailed error information and execution traces.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is available under the MIT License. See the LICENSE file for more details.

## Future Enhancements

- [ ] Web-based interface
- [ ] Support for different VM operating systems
- [ ] Resource monitoring and usage statistics
- [ ] VM clustering and networking simulation
- [ ] Integration with cloud providers APIs
- [ ] Advanced provisioning with Ansible/Chef support