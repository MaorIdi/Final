from machine import VirtualMachine
from pydantic import ValidationError
import json
import os 
import logging as logger
import subprocess
instances_config_path = '../configs/instances.json'

log_formatter = logger.Formatter(
    '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logs_dir = '../logs'
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

file_handler = logger.FileHandler('../logs/provisioning.log', mode='a')
file_handler.setLevel(logger.DEBUG)
file_handler.setFormatter(log_formatter)

console_handler = logger.StreamHandler()
console_handler.setLevel(logger.DEBUG)
console_handler.setFormatter(log_formatter)

logger.basicConfig(level=logger.DEBUG, handlers=[file_handler, console_handler])


def ask_user_for_vms():
    separator = '\n' + '-'*50 + '\n'


    flag = input("Would you like to create a new virtual machine (y/n): ")
    vms = []

    while flag.lower() == 'y':
        try:
            vm_name = input('Enter the nickname of the VM: ')
            cpu = input('Enter the number of CPUs: ')
            memory = input('Enter the amount of memory (in MB): ')
            disk = input('Enter the size of the disk (in GB): ')

            print(separator)

            try:        
                vm = VirtualMachine(
                    name=vm_name,
                    cpu=cpu,
                    memory=memory,
                    disk=disk
                )

                logger.info(f'Virtual Machine created: {vm}')
                vms.append(dict(vm))
                print(separator)


            except ValidationError as e:
                for error in e.errors():
                    logger.warning(f"Validation error for field '{error['loc'][0]}': {error['msg']}")
                
                print(separator)
            except Exception:
                logger.error('Something went wrong, please try again later..')
            finally:
                flag = input("Would you like to create another virtual machine? (y/n): ")
                
        except Exception as e:
            logger.error("Something went wrong please try again later..")
            logger.error(f'error: {e}')
    return vms



def dump_vms(vms):
    if vms:
        global instances_config_path
        vms_obj = {"vms": vms}


        configs_dir = '../configs'
        if not os.path.exists(configs_dir):
            os.makedirs(configs_dir)

        if not os.path.exists(instances_config_path):
            with open(instances_config_path, 'w') as f:
                json.dump(vms_obj, f)
                return


        try:
            with open(instances_config_path, 'r') as f:
                data = json.load(f)

                try:
                    vms_list = data['vms']
                except KeyError:
                    vms_list = []

                for vm in vms:
                    vms_list.append(vm)

            with open(instances_config_path, 'w') as f:
                json.dump(data, f)  


        except json.decoder.JSONDecodeError:
            with open(instances_config_path, 'w') as f:
                json.dump(vms_obj, f)

        logger.info(f'Done dumping vms to {instances_config_path}')



def configure_vm(vm):
    try:
        result = subprocess.run(['bash', '../scripts/init_vm.sh', str(vm)], capture_output=True, text=True)
        logger.info(f"init_vm.sh output: {result.stdout.strip().replace('\n', ' - ')}")
        if result.stderr:
            logger.warning(f"init_vm.sh errors: {result.stderr.strip()}")
    except Exception as e:
        logger.error(f"Something went wrong while running init_vm.sh: {e}")


def configure_vms_from_file(path):
    with open(path, 'r') as f:
        data = json.load(f)
        vm_list = data['vms']

    for vm in vm_list:
        configure_vm(vm['name'])
        # vm_list.remove(vm)

        # with open(path, 'w') as f:
        #     data['vms'] = vm_list
        #     json.dump(data, f)



def main():
    global instances_config_path
    vms = ask_user_for_vms()
    dump_vms(vms)
    configure_vms_from_file(instances_config_path)


    
    

if __name__ == '__main__':
    main()