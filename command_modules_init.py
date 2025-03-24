import pkgutil
import importlib
import command_modules
# from config import ENABLED_MODULES

all_commands = {}
all_commands_str = ""
additional_info_str = ""

# Iterate over all modules in the handlers package
print(("Loaded command modules:"))
for _, module_name, _ in pkgutil.iter_modules(command_modules.__path__, command_modules.__name__ + "."):

    # if (module_name.split('.')[-1] not in ENABLED_MODULES): continue

    module = importlib.import_module(module_name)
    print(module_name)
    # Merge the command_handlers from each module
    if hasattr(module, "command_handlers"):
        all_commands.update(module.command_handlers)

    if hasattr(module, "commands_string"):
        all_commands_str += module.commands_string + '\n'

    if hasattr(module, "additional_info"):
        additional_info_str += module.additional_info + '\n'

