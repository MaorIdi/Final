# Virtual Machine Infrastructure Simulator 🖥️

A Python-based virtual machine infrastructure simulator that provides an interactive command-line interface for creating, configuring, and managing virtual machines. This tool is perfect for learning infrastructure concepts, testing deployment workflows, or simulating VM environments without the overhead of actual virtualization.

## ✨ Features

- **Interactive VM Creation**: Create virtual machines by specifying CPU, memory, and disk requirements through an intuitive CLI
- **Data Validation**: Robust input validation using Pydantic models to ensure data integrity and type safety
- **Configuration Persistence**: Automatically save VM configurations to JSON files for reuse and batch operations
- **Automated Provisioning**: Simulate VM setup and software installation with customizable shell scripts (Nginx simulation included)
- **Smart Logging System**: Flexible logging with environment variable control - supports console output, file logging, or logs-only mode
- **Batch Processing**: Configure multiple VMs from saved configuration files
- **Error Recovery**: Comprehensive error handling with detailed logging and graceful failure recovery

## 📁 Project Structure

```
Final/
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── run.sh                     # Convenience script to run the application
├── configs/
│   └── instances.json         # VM configurations storage (auto-generated)
├── logs/
│   └── provisioning.log       # Application logs (auto-generated)
├── scripts/
│   └── init_vm.sh            # VM initialization script (Nginx installation simulation)
└── src/
    ├── infra_simulator.py     # Main application logic and entry point
    ├── machine.py            # VM data model using Pydantic
    └── __pycache__/          # Python cache files (auto-generated)
```

## 🔧 Requirements

- **Python**: 3.7 or higher
- **Operating System**: Linux, macOS, or Windows with WSL
- **Shell**: Bash (for running initialization scripts)
- **Dependencies**: Listed in `requirements.txt` (auto-installed)

## 🚀 Installation

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/MaorIdi/Final.git
   cd Final
   ```

2. **Set up virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Make scripts executable** (Linux/macOS)
   ```bash
   chmod +x run.sh scripts/init_vm.sh
   ```

### Verification

Test your installation:
```bash
python src/infra_simulator.py --help 2>/dev/null || echo "Ready to run!"
```

## 🎮 Usage

### Running the Simulator

Choose your preferred method to run the simulator:

**Method 1: Using the convenience script (Recommended)**
```bash
./run.sh
```
*Note: This automatically activates the virtual environment and runs the application*

**Method 2: Direct execution**
```bash
cd src
python infra_simulator.py
```

**Method 3: With custom logging configuration**
```bash
# Console + file logging (default)
LOGGING_MODE=console python src/infra_simulator.py

# File-only logging (quiet mode)
LOGGING_MODE=logs_only python src/infra_simulator.py
```

### 🎯 Interactive VM Creation Process

The application guides you through an intuitive workflow:

1. **Initial Prompt**: Choose whether to create a new virtual machine
2. **VM Configuration**: Specify the following details:
   - **VM Nickname**: A unique, descriptive identifier (spaces automatically converted to hyphens)
   - **CPU Cores**: Number of virtual CPU cores (accepts decimal values, e.g., 2.5)
   - **Memory (MB)**: RAM allocation in megabytes (e.g., 4096 for 4GB)
   - **Disk Space (GB)**: Storage capacity in gigabytes (e.g., 50)

3. **Validation & Creation**: The system validates inputs and creates the VM
4. **Continue or Finish**: Option to create additional VMs or proceed to provisioning

### 💡 Example Interactive Session

```
Would you like to create a new virtual machine (y/n): y
Enter the nickname of the VM: web-server-01
Enter the number of CPUs: 2
Enter the amount of memory: 4096
Enter the size of the disk: 50

--------------------------------------------------

Virtual Machine created: name='web-server-01' cpu=2.0 memory=4096.0 disk=50.0

--------------------------------------------------

Would you like to create another virtual machine? (y/n): n

Installing Nginx on: 'web-server-01'
Installation finished successfully.
Done dumping vms to /path/to/Final/configs/instances.json
```

## 📄 Configuration Files

### VM Instances Storage (`configs/instances.json`)

The application automatically saves all VM configurations in a structured JSON format:

```json
{
  "vms": [
    {
      "name": "web-server-01",
      "cpu": 2.0,
      "memory": 4096.0,
      "disk": 50.0
    },
    {
      "name": "database-server",
      "cpu": 4.0,
      "memory": 8192.0,
      "disk": 100.0
    }
  ]
}
```

### Dependencies (`requirements.txt`)

The project uses these carefully selected dependencies:

```
annotated-types==0.7.0      # Enhanced type annotations
pydantic==2.11.7           # Data validation and parsing using Pydantic v2
pydantic_core==2.33.2      # Core functionality for Pydantic
typing-inspection==0.4.1   # Runtime type inspection utilities
typing_extensions==4.14.1  # Extended typing support for older Python versions
```

## 📊 Logging System

### Logging Modes

The application offers flexible logging configurations:

| Mode | Console Output | File Output | Use Case |
|------|----------------|-------------|----------|
| **console** (default) | ✅ Yes | ✅ Yes | Development, debugging |
| **logs_only** | ❌ No | ✅ Yes | Production, automation |

### Environment Variable Control

Configure logging behavior using the `LOGGING_MODE` environment variable:

```bash
# Method 1: Inline variable
LOGGING_MODE=console python src/infra_simulator.py

# Method 2: Export for session
export LOGGING_MODE=logs_only
python src/infra_simulator.py

# Method 3: Using .env file (if implemented)
echo "LOGGING_MODE=logs_only" > .env
```

### Log Format & Structure

```
2025-07-31 10:30:45 - INFO - root - Virtual Machine created: name='web-server-01' cpu=2.0 memory=4096.0 disk=50.0
2025-07-31 10:30:46 - INFO - root - init_vm.sh output: Installing Nginx on: 'web-server-01' - Installation finished successfully.
```

**Log Levels:**
- **INFO**: Successful operations, VM creation, configuration saves
- **WARNING**: Validation errors, non-critical issues, file creation warnings
- **ERROR**: Critical failures, script execution errors, file system issues

## ⚙️ VM Provisioning System

### Automatic Provisioning Workflow

1. **VM Creation**: After successful VM validation and storage
2. **Script Execution**: Runs `scripts/init_vm.sh` for each VM
3. **Progress Tracking**: Logs all provisioning steps and outcomes
4. **Error Handling**: Gracefully handles script failures without stopping the process

### Provisioning Script (`scripts/init_vm.sh`)

**Current Functionality:**
- Simulates Nginx web server installation
- Provides realistic installation timing (2-second delay)
- Returns appropriate exit codes for error handling

**Customization:**
```bash
# Example: Extend the script for multiple services
#!/bin/bash
vm_name=$1

if [[ ! -z $vm_name ]]; then
    echo "Provisioning VM: '$vm_name'"
    
    # Install Nginx
    echo "Installing Nginx..."
    sleep 2
    echo "Nginx installed successfully"
    
    # Install Docker (example)
    echo "Installing Docker..."
    sleep 3
    echo "Docker installed successfully"
    
    echo "Provisioning completed for '$vm_name'"
else
    echo "Error: VM name is required"
    exit 1
fi
```

## 🏗️ Architecture & Data Model

### VM Data Structure

Virtual machines are represented using Pydantic models with strict typing and validation:

```python
from pydantic import BaseModel

class VirtualMachine(BaseModel):
    name: str      # VM identifier (spaces auto-converted to hyphens)
    cpu: float     # Number of CPU cores (supports fractional cores)
    memory: float  # Memory allocation in MB
    disk: float    # Disk capacity in GB
    
    # Automatic validation ensures:
    # - All fields are present and properly typed
    # - Numeric values are converted to float
    # - Name normalization (spaces → hyphens)
```

### Key Components

| Component | Purpose | Key Features |
|-----------|---------|--------------|
| `infra_simulator.py` | Main application logic | Interactive CLI, logging, VM management |
| `machine.py` | Data model definition | Pydantic validation, type safety |
| `init_vm.sh` | Provisioning script | Customizable VM setup simulation |
| `instances.json` | Configuration storage | Persistent VM configurations |

## 🛡️ Error Handling & Validation

### Input Validation

The application provides comprehensive validation:

- **Data Type Validation**: Automatic conversion and type checking via Pydantic
- **Required Fields**: Ensures all VM properties are specified
- **Name Normalization**: Converts spaces to hyphens for system compatibility
- **Numeric Validation**: Accepts both integer and decimal values for resources

### Error Recovery

```python
# Example validation error output:
Validation error for field 'cpu': Input should be a valid number
Validation error for field 'memory': Field required
```

### Common Error Scenarios

1. **Invalid Input Types**: Non-numeric values for CPU/memory/disk
2. **Empty Fields**: Missing required VM properties
3. **File System Issues**: Permission problems, disk space
4. **Script Execution**: Provisioning script failures

## 🔨 Development & Customization

### Extending VM Properties

Add new properties to the VM model:

```python
# In machine.py
class VirtualMachine(BaseModel):
    name: str
    cpu: float
    memory: float
    disk: float
    operating_system: str = "Ubuntu 22.04"  # New field with default
    network_interfaces: int = 1              # New field
```

### Custom Provisioning Scripts

Create specialized provisioning for different VM types:

```bash
# scripts/init_database_vm.sh
#!/bin/bash
vm_name=$1
echo "Setting up database server: $vm_name"
# Add MySQL/PostgreSQL installation simulation
sleep 3
echo "Database server ready"

# scripts/init_web_vm.sh
#!/bin/bash
vm_name=$1
echo "Setting up web server: $vm_name"
# Add Apache/Nginx + PHP installation simulation
sleep 4
echo "Web server configured"
```

### Development Mode

Run with enhanced debugging:

```bash
# Enable detailed logging
export PYTHONPATH=$PWD/src
export LOGGING_MODE=console
python -u src/infra_simulator.py

# Or use development script
./run_dev.sh  # Create this script for development shortcuts
```

## 🐛 Troubleshooting Guide

### Installation Issues

**Problem**: `ModuleNotFoundError: No module named 'pydantic'`
```bash
# Solution:
pip install -r requirements.txt
# Or for development:
pip install -e .
```

**Problem**: `Permission denied: ./run.sh`
```bash
# Solution:
chmod +x run.sh scripts/init_vm.sh
```

### Runtime Issues

**Problem**: `FileNotFoundError: [Errno 2] No such file or directory: '../configs'`
```bash
# Solution: The application auto-creates directories, but if issues persist:
mkdir -p configs logs
```

**Problem**: Validation errors for numeric inputs
```bash
# Solution: Ensure inputs are numeric
Enter the number of CPUs: 2      # ✅ Correct
Enter the number of CPUs: two    # ❌ Invalid
```

### Logging Issues

**Problem**: No console output in `logs_only` mode
```bash
# This is expected behavior. To see output:
LOGGING_MODE=console python src/infra_simulator.py
# Or check the log file:
tail -f logs/provisioning.log
```

**Problem**: Log file not created
```bash
# Check permissions and create directory:
mkdir -p logs
touch logs/provisioning.log
chmod 644 logs/provisioning.log
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup

1. **Fork and clone**
   ```bash
   git clone https://github.com/yourusername/Final.git
   cd Final
   ```

2. **Create development environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Create feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Code Style Guidelines

- Follow PEP 8 for Python code formatting
- Use type hints where appropriate
- Add docstrings for new functions
- Maintain backward compatibility
- Include tests for new features

### Pull Request Process

1. **Test your changes**
   ```bash
   python src/infra_simulator.py  # Manual testing
   # Add automated tests if applicable
   ```

2. **Update documentation** if needed
3. **Submit pull request** with clear description of changes

## 📋 Roadmap & Future Enhancements

### Planned Features

- [ ] **Web Interface**: Browser-based VM management dashboard
- [ ] **Multiple OS Support**: Windows, CentOS, Debian VM templates
- [ ] **Resource Monitoring**: CPU, memory, disk usage simulation
- [ ] **Network Simulation**: VM networking and connectivity modeling
- [ ] **Cloud Integration**: AWS, Azure, GCP provider simulation
- [ ] **Cluster Management**: Multi-VM orchestration and load balancing
- [ ] **Advanced Provisioning**: Ansible, Chef, Puppet integration
- [ ] **Export/Import**: VM template sharing and backup functionality
- [ ] **Performance Metrics**: Benchmarking and resource optimization

### Version History

- **v1.0.0**: Initial release with basic VM creation and provisioning
- **v1.1.0**: Enhanced logging system with environment variable control
- **v1.2.0**: Improved error handling and validation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
- ✅ Commercial use allowed
- ✅ Modification allowed  
- ✅ Distribution allowed
- ✅ Private use allowed
- ❗ License and copyright notice required

## 🙋‍♂️ Support & Contact

- **Issues**: [GitHub Issues](https://github.com/MaorIdi/Final/issues)
- **Discussions**: [GitHub Discussions](https://github.com/MaorIdi/Final/discussions)
- **Email**: Create an issue for direct contact

---

**Made with ❤️ by [MaorIdi](https://github.com/MaorIdi)**

*Star this repository if you found it helpful! ⭐*