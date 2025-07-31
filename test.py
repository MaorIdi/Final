from pathlib import Path
def get_absolute_path(relative):
    current_path = Path(__file__).parent
    return (current_path / relative).resolve()


config_path = get_absolute_path('../scripts/init_vm.sh')

print(config_path)