# Virtual Machine Infrastructure Simulator

A Python-based virtual machine infrastructure simulator that allows users to create, configure, and manage virtual machines through an interactive command-line interface.

## Features

- **Interactive VM Creation**: Create virtual machines by specifying CPU, memory, and disk requirements
- **Data Validation**: Input validation using Pydantic models to ensure data integrity
- **Configuration Persistence**: Save VM configurations to JSON files for later use
- **Automated Provisioning**: Simulate VM setup and software installation (Nginx simulation included)
- **Comprehensive Logging**: Detailed logging system with both file and console output
- **Batch Processing**: Configure multiple VMs from saved configuration files

## Project Structure

```
Final/
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── configs/
│   └── instances.json         # VM configurations storage
├── logs/
│   └── provisioning.log       # Application logs
├── scripts/
│   └── init_vm.sh            # VM initialization script (Nginx installation simulation)
└── src/
    ├── infra_simulator.py     # Main application logic
    ├── machine.py            # VM data model
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

Navigate to the `src` directory and run the main script:

```bash
cd src
python infra_simulator.py
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

Key dependencies:
- `pydantic`: Data validation and parsing
- `annotated-types`: Type annotations support
- `typing-extensions`: Extended typing support

## Logging

The application provides comprehensive logging:

- **Console Output**: Real-time feedback during execution
- **Log File**: Persistent logging in `logs/provisioning.log`
- **Log Levels**: INFO, WARNING, ERROR for different event types

### Log Format

```
2025-01-27 10:30:45 - INFO - root - Virtual Machine created: name='web-server-01' cpu=2.0 memory=4096.0 disk=50.0
```

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

For development purposes, you can modify the logging level or add additional debug information by editing the logging configuration in `infra_simulator.py`.

## Troubleshooting

### Common Issues

1. **Permission Denied (init_vm.sh)**
   ```bash
   chmod +x scripts/init_vm.sh
   ```

2. **Module Not Found**
   ```bash
   pip install -r requirements.txt
   ```

3. **Invalid Input Values**
   - Ensure CPU, memory, and disk values are numeric
   - Check that VM names are unique and non-empty

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